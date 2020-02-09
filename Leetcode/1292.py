from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        cms = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

                cms += 1
                if not (cms <= i and cms <= j
                        and threshold >= dp[i][j] + dp[i - cms][j - cms] - dp[i - cms][j] - dp[i][j - cms]):
                    cms -= 1

        for line in dp:
            print(line)
        return cms


if __name__ == '__main__':
    sol = Solution()
    matr = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    t = 4

    m2 = [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 1, 2]]
    t2 = 1
    print(sol.maxSideLength(m2, t2))
