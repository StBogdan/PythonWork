from typing import List


class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        islands = 0

        n = len(grid)
        m = len(grid[0])

        def global_warm(grid_mod, i, j):
            stillIsland = True

            if grid_mod[i][j] == 0:
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    stillIsland = False

                grid_mod[i][j] = 1
                if i > 0:
                    stillIsland &= global_warm(grid_mod, i - 1, j)
                if j > 0:
                    stillIsland &= global_warm(grid_mod, i, j - 1)
                if i < n - 1:
                    stillIsland &= global_warm(grid_mod, i + 1, j)
                if j < m - 1:
                    stillIsland &= global_warm(grid_mod, i, j + 1)

            return stillIsland

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    newIsland = True

                    # Edge square
                    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                        newIsland = False

                    if newIsland and global_warm(grid, i, j):
                        islands += 1

        return islands


if __name__ == '__main__':
    grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    sol = Solution()
    print(f"Ans: {sol.closedIsland(grid)}")
