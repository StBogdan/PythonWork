from typing import List

# Name: Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Method: Keep track of max combo, and minimum too (for negatives), also see w/ current (for 0s)
# Time: O(n)
# Space: O(1)
# Difficulty: Medium


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = max_now = min_now = nums[0]

        for i in range(1, len(nums)):
            elem = nums[i]
            new_from_max = max_now * elem
            new_from_min = min_now * elem

            min_now = min(elem, new_from_min, new_from_max)
            max_now = max(elem, new_from_min, new_from_max)
            res = max(max_now, res)

        return res
