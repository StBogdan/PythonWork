from typing import List

# Name: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Method: Store complement (for 3sum+, sorting works)
# Time: O(n)
# Space: O(n)
# Difficulty: Easy


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            if nums[i] in complements:
                return [complements[nums[i]], i]
            else:
                complements[-nums[i] + target] = i
