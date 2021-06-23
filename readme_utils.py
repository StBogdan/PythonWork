import click
import os
import re
# Read a file
from typing import IO, Optional

PROPERTY_PATTERNS = {
    "title": r"# Name: (.*)\n",
    "url": r"# Link: (.*)\n",
    "time_complexity": r"# Time: (.*)\n",
    "space_complexity": r"# Space: (.*)\n",
    "difficulty": r"# Difficulty: (.*)\n",
}


def readFile(fileName):
    file = open(fileName)
    content = file.read()
    return content


@click.group()
def cli():
    pass


@cli.command()
@click.option("--number", "-n")
@click.option("--title", "-t")
@click.option("--url", "-u")
@click.option("--difficulty", "-d")
@click.option("--time_complexity", "-tc")
@click.option("--space_complexity", "-sc")
@click.option("--notes")
def table_entry_lc(number: str,
                   title: str,
                   url: str,
                   difficulty: str,
                   time_complexity: str,
                   space_complexity: str,
                   notes: str = ""):
    """ Create a markdown table entry from params"""
    markdown_line = build_lc_line(number, title, url, difficulty,
                                  time_complexity, space_complexity, notes)
    click.echo(markdown_line)


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


def file_to_int(lc_file: str) -> int:
    try:
        file_name , _ = lc_file.rsplit(".", 1) 
        return int(file_name)
    except ValueError:
        return 999999

@cli.command()
@click.option("--outputfile", "-o")
def backfill_lc(outputfile: str):
    """Look in the Leetcode folder, 
    generate table entries for files there:
    If they have expected lines
    """
    lc_folder = "Leetcode"

    entries = []
    all_py_solutions = [x for x in os.listdir(lc_folder) if x.endswith(".py")]

    all_py_solutions_sorted = sorted(all_py_solutions, key=file_to_int)

    for file in all_py_solutions_sorted:
        print(f"Looking at file {file:20}", end="... ")
        with open(os.path.join(lc_folder, file), "r") as f:
            maybe_entry = get_entry_from_file(f)
            if maybe_entry:
                entries.append(maybe_entry)

    print(f"Out of {len(list(all_py_solutions))}, "
          f"got descriptions for {len(entries)}")

    if outputfile:
        with open(outputfile, "w+") as of:
            of.write("\n".join(entries))
            click.echo(f"Results written in {outputfile}")
    else:
        for entry in entries:
            print(entry)


def get_entry_from_file(file: IO) -> Optional[str]:
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
        return build_lc_line(number, **problem_details)
    else:
        print(f"Properties missing, found: {problem_details}")


if __name__ == "__main__":
    cli()
