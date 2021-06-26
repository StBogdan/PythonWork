from typing import List

# Name: Parallel Courses
# Link: https://leetcode.com/problems/parallel-courses/
# Method: Topological sort, level based on courses w/o prereq
# Time: O(V + E)
# Space: O(V + E)
# Difficulty: Medium
# Notes: V = nr. courses = n and E = nr. relations


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        if not relations:
            return 0
        graph = {x: {"in": set(), "out": set()} for x in range(1, n + 1)}
        for a, b in relations:
            graph[a]["out"].add(b)
            graph[b]["in"].add(a)

        sems = 0
        level = {c for c in graph if not graph[c]["in"]}
        while level:
            sems += 1
            next_level = set()
            for course in level:
                for next_course in graph[course]["out"]:
                    graph[next_course]["in"].remove(course)
                    if not graph[next_course]["in"]:
                        next_level.add(next_course)
            level = next_level

        return -1 if any(graph[course]["in"] for course in graph) else sems

