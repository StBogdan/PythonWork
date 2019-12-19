from functools import lru_cache


class Solution:
    zero_ways = 0

    def numWays(self, steps: int, arrLen: int) -> int:

        @lru_cache(None)
        def step(poz: int, steps: int):
            if poz < 0 or steps < 0 or poz >= arrLen or steps < poz:
                return 0
            elif poz == steps:
                return 1
            else:
                return step(poz + 1, steps - 1) + step(poz - 1, steps - 1) + step(poz, steps - 1)

        return step(0, steps) % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numWays(15, 15))
