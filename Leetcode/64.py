from typing import List

# Name: Minimum Path Sum
# Link: https://leetcode.com/problems/minimum-path-sum/
# Method: DP for minimum path to given matrix poz
# Time: O(n\*m)
# Space: O(n\*m)
# Difficulty: Medium


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sm = [[0] * cols for _ in range(rows)]
        # print(sm)

        ts = 0
        for col in range(cols):
            ts += grid[0][col]
            sm[0][col] = ts

        ts = 0
        for row in range(rows):
            ts += grid[row][0]
            sm[row][0] = ts

        for row in range(1, rows):
            for col in range(1, cols):
                to_get_here = min(sm[row - 1][col], sm[row][col - 1])
                sm[row][col] = to_get_here + grid[row][col]

        # for row in sm:
        #     print(row)
        return sm[rows - 1][cols - 1]


if __name__ == "__main__":
    sol = Solution()

    inp = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(inp))
