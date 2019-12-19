from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        reach = 0
        n = len(grid)
        m = len(grid[0])
        # Line pass
        for line in grid:
            online = 0
            first = -1
            for j in range(m):
                if line[j] != 0:
                    online += 1
                    # Uninit
                    line[j] = -1
                    if first == -1:
                        first = j

            if online == 1:
                line[first] = 1

        for j in range(m):
            online = 0
            first = -1
            fval = None
            for j in range(n):
                if grid[j][j] != 0:
                    online += 1
                    # Uninit
                    if first == -1:
                        first = j
                        fval = grid[j][j]
                    grid[j][j] = -1

            print(f"Online on line {online}")
            if online == 1 and fval == 1:
                grid[first][j] = 1

        for line in grid:
            reach += line.count(-1)

        return reach


if __name__ == '__main__':
    grid = [[1, 0], [1, 1]]
    sol = Solution()
    print(sol.countServers(grid))
