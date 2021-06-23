from typing import List

# Name: House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/
# Method: Look at raidable houses, do 2 calls to regular solution
# Time: O(n)
# Space: O(1)
# Difficulty: Medium


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(
            self.rob_linear(nums, 0, len(nums) - 2),
            self.rob_linear(nums, 1, len(nums) - 1),
        )

    @staticmethod
    def rob_linear(houses: List[int], start: int, end: int) -> int:
        # Compressed DP, look at the previous 2 house rob values
        ante_prev = 0
        prev = 0
        for i in range(start, end + 1):
            house_now = max(houses[i] + ante_prev, prev)
            ante_prev = prev
            prev = house_now
        return prev
