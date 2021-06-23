from typing import List

# Name: Valid Square
# Link: https://leetcode.com/problems/valid-square/
# Method: Math, find all distances, 4 sides and 2 diagonals
# Time: O(1)
# Space: O(1)
# Difficulty: Medium


Point = List[int]

class Solution:
    @staticmethod
    def point_distance(p1: Point, p2: Point) -> float:
        return abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        dist = []
        for i in range(3):
            for j in range(i+1, 4):
                if points[i] == points[j]:
                    return False
                dist.append(self.point_distance(points[i], points[j]))
        dist.sort()

        return dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5]
