from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        sm = [[0] * m for _ in range(n)]
        print(sm)

        ts = 0
        for j in range(m):
            ts += grid[0][j]
            sm[0][j] = ts

        ts = 0
        for i in range(n):
            ts += grid[i][0]
            sm[i][0] = ts

        for i in range(1, n):
            for j in range(1, m):
                tgh = min(sm[i - 1][j], sm[i][j - 1])
                sm[i][j] = tgh + grid[i][j]

        for row in sm:
            print(row)
        return sm[n - 1][m - 1]


if __name__ == "__main__":
    sol = Solution()

    inp = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(inp))
