# Name:  Peak Index in a Mountain Array
# Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Method: Binary search
# Time: O(log(n))
# Space: O(1)
# Difficulty: Easy

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l
