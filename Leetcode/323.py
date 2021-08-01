from collections import defaultdict
from typing import List

# Name: Number of Connected Components in an Undirected Graph
# Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Method: DFS from every node to n
# Time: O(n)
# Space: O(n + e)
# Difficulty: Medium
# Note: n = nr of nodes, e = nr of edges


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        comps = 0
        seen = set()
        for node in range(n):
            if node in seen:
                continue

            comps += 1
            to_visit = [node]
            seen.add(node)
            while to_visit:
                node_now = to_visit.pop()

                for vecin in graph[node_now]:
                    if vecin not in seen:
                        to_visit.append(vecin)
                        seen.add(vecin)

        return comps
