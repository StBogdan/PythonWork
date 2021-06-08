from typing import List

# Name: Coin Change
# Link: https://leetcode.com/problems/coin-change/
# Method: DP, build to the target amount
# Time: O(m \* n)
# Space: O(m)
# Difficulty: Medium
# Notes: m = amount, n = nr of coins


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        way_to_reach = [-1] * (amount + 1)
        way_to_reach[0] = 0
        for i in range(1, amount + 1):
            ways = [
                way_to_reach[i - coin]
                for coin in coins
                if i - coin >= 0 and way_to_reach[i - coin] != -1
            ]
            if ways:
                way_to_reach[i] = min(ways) + 1

        return way_to_reach[amount]
