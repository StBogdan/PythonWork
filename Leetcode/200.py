from typing import List

# Method: Traverse islands, mark as null
# Time: O(n*m)
# Space: O(n*m)

DIRS = [[0, 1], [0, -1], [-1, 0], [1, 0]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])

        def explore_isle(i, j):
            grid[i][j] = '2'
            for oi, oj in DIRS:
                i2 = i+oi
                j2 = j+oj
                if not (i2 < 0 or j2 < 0 or i2 >= n or j2 >= m) \
                        and grid[i2][j2] == '1':
                    explore_isle(i2, j2)

        isles = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    explore_isle(i, j)
                    isles += 1
        return isles

if __name__ == "__main__":
    a = [['1', '1', '0', '1', '0'],
         ['1', '1', '0', '0', '1'],
         ['1', '1', '0', '0', '0'],
         ['1', '1', '1', '1', '1'], ]
    sol = Solution()
    print(sol.numIslands(a))
