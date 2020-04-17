from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def exp_isle(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            print(f"Checking {i} {j}")
            if grid[i][j] == "1":
                grid[i][j] = "2"
                for oi, oj in directions:
                    exp_isle(i + oi, j + oj)

        isles = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(f"Now at {i} {j} w/ val {grid[i][j]}")
                if grid[i][j] == "1":
                    print(f"Isle at {i} {j}")
                    isles += 1
                    exp_isle(i, j)
        return isles


if __name__ == "__main__":
    a = [['1', '1', '0', '1', '0'],
         ['1', '1', '0', '0', '1'],
         ['1', '1', '0', '0', '0'],
         ['1', '1', '1', '1', '1'], ]
    sol = Solution()
    print(sol.numIslands(a))
