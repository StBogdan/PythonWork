from typing import List
import unittest


# Name: Best Time to Buy and Sell Stock IV
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Method: Dynamic programming, crying and reading the solutions
# Time: O(n*k)
# Space: O(n*k)
# Difficulty: Hard


class Solution:
    def maxProfit(self, ts: int, array: List[int]) -> int:
        if not array or not ts:
            return 0

        n = len(array)

        dp = [[[float("-inf")] * 2 for _ in range(ts + 1)] for _ in range(n)]

        # 0 is paper hands
        # 1 is hold 💎✋

        dp[0][0][0] = 0
        dp[0][1][1] = -array[0]

        for i in range(1, n):
            for j in range(ts + 1):  # TODO Worry about padding
                dp[i][j][0] = max(
                    dp[i - 1][j][0], dp[i - 1][j][1] + array[i]  # Keep not holding
                )  # Sell the stock
                if j > 0:  # No previous transaction, can't start a new one
                    dp[i][j][1] = max(
                        dp[i - 1][j][1], dp[i - 1][j - 1][0] - array[i]  # Keep holding
                    )  # Start holding by buying the stock

        for day, line in enumerate(dp):
            print(f"Day {day}: ", end=" ")
            for paper, diamond in line:
                print(f"📰:{paper:4} 💎:{diamond:4}", end=" | ")
            print()

        return max(dp[n - 1][tsi][0] for tsi in range(ts + 1))


class TestStonks(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_transaction_2(self):
        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        self.assertEqual(self.sol.maxProfit(k, prices), 7)

    def test_transactions_k_more_than_half(self):
        k = 6
        prices = [1, 2, 3, 4, 5, 3, 2, 1]
        self.assertEqual(self.sol.maxProfit(k, prices), 4)


unittest.main()


# dp[day][transactions] [hold, sell,  buy]

# dp[day][transactions] [hold] = max(0, dp[day-1][transactions][hold], dp[day-1][transactions][hold]

# dp[d][t][a]

# dp[d][t][buy] = max(aray[d] + dp[d-1][t-1][0]

# dp[d][t][hold] = dp[d-1][t][hold]
# dp[d][t][not hold] = dp[d-1][t][not hold]

# dp[d][t][not hold] = dp[d-1][t-1][hold] - array[d] # Buy
# dp[d][t][not hold] = dp[d-1][t][hold]   + array[d] # Sell


# dp[d][t][not hold] = max(dp[d-1][t-1][hold] - array[d], dp[d-1][t][hold]   + array[d]

# dp[d][t][hold] = max(dp[d-1][t][hold], dp[d-1][t][not hold] + array[d])
# dp[d][t][not hold] = max(dp[d-1][t][not hold], dp[d-1][t-1][hold] - array[d])`
