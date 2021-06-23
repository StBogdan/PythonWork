from typing import List

# Name: Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Method: Compressed DP, previous largest subsequence
# Time: O(n\*log(n))
# Space: O(n)
# Difficulty: Medium


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = [nums[0]]
        for i in range(1, len(nums)):
            insert_poz = self.bisect(seq, nums[i])
            if insert_poz == len(seq):
                seq.append(nums[i])
            else:
                seq[insert_poz] = nums[i]

        return len(seq)

    @staticmethod
    def bisect(arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > arr[mid]:
                low = mid + 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                return mid

        return low
