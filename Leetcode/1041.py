# Name: Robot Bounded In Circle
# Link: https://leetcode.com/problems/robot-bounded-in-circle/
# Method: Simulate moves, check final position and heading (if not UP, will cycle)
# Time: O(n)
# Space: O(1)
# Difficulty: Medium

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Up, right, down, left


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        poz_now = (0, 0)
        dir_now = 0

        for cmd in instructions:
            if cmd == "G":
                poz_now = (poz_now[0] + DIRS[dir_now][0], poz_now[1] + DIRS[dir_now][1])
            elif cmd == "L":
                dir_now = (dir_now - 1) % 4
            else:
                dir_now = (dir_now + 1) % 4

        return poz_now == (0, 0) or dir_now != 0
