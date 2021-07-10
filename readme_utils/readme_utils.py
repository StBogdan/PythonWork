import os
import re
# Read a file
from typing import Callable, IO, Optional

PROPERTY_PATTERNS = {
    "title": r"# Name: (.*)\n",
    "url": r"# Link: (.*)\n",
    "time_complexity": r"# Time: (.*)\n",
    "space_complexity": r"# Space: (.*)\n",
    "difficulty": r"# Difficulty: (.*)\n",
}


def build_lc_line(number: str,
                  title: str,
                  url: str,
                  difficulty: str,
                  time_complexity: str,
                  space_complexity: str,
                  notes: str = "") -> str:
    problem_link = f"[{title}]({url})"
    return f"| {number:4} | {problem_link:143} | [Python](./Leetcode/{number}.py) 	| " + \
        f"{difficulty} | {time_complexity} 	| {space_complexity} 	| {notes} 	| "

def build_cf_line(number: str,
                  title: str,
                  url: str,
                  difficulty: str,
                  time_complexity: str,
                  space_complexity: str,
                  notes: str = "") -> str:
    problem_link = f"[{title}]({url})"
    return f"| {number:4} | {problem_link:143} | [Python](./CodeForces/{number}.py)  | " + \
        f"{difficulty} | {time_complexity} 	| {space_complexity} 	| {notes} 	| "


def file_to_int(lc_file: str) -> int:
    try:
        file_name , _ = lc_file.rsplit(".", 1) 
        return int(file_name)
    except ValueError:
        return 999999



def get_entry_from_file(file: IO, line_gen_func: Callable) -> Optional[str]:
    raw_text = file.read()
    problem_details = {}

    for name, pattern in PROPERTY_PATTERNS.items():
        match = re.search(pattern, raw_text)
        if match:
            problem_details[name] = match.group(1)

        # print(f"Looking for {name} w/ pattern {pattern}, got match {match}")

    if len(problem_details) == len(PROPERTY_PATTERNS):
        print("Found all of them, creating markdown")

        _, filename = os.path.split(file.name)
        number, _ = filename.split('.')
        return line_gen_func(number, **problem_details)
    else:
        print(f"Properties missing, found: {problem_details}")


