from typing import Tuple, List

# Name: Minimum Area Rectangle
# Link: https://leetcode.com/problems/minimum-area-rectangle/
# Method: For every pair, check if can form rectangle
# Time: O(n^2)
# Space: O(n)
# Difficulty: Medium


Point = Tuple[int, int]


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        min_rectangle = float("inf")
        for x1, y1 in points:
            for x2, y2 in point_set:  # For all previous points
                if (x2, y1) in point_set and (x1, y2) in point_set:
                    rect_area = abs((x2 - x1) * (y2 - y1))
                    if rect_area:
                        min_rectangle = min(rect_area, min_rectangle)

            point_set.add((x1, y1))

        return min_rectangle if min_rectangle != float("inf") else 0
