from typing import List
import unittest
from collections import defaultdict

# Name: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Method: Prefix sum, store number of ways to get to a sum, check against target 
# Time: O(n)
# Space: O(n)
# Difficulty: Medium


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumseen = defaultdict(int)
        sum_now = 0
        nr_arrs = 0
        for x in nums:
            sum_now += x
            if sum_now == k:
                nr_arrs += 1
            if sum_now - k in sumseen:
                nr_arrs += sumseen[sum_now-k]
            sumseen[sum_now] += 1
        return nr_arrs



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_negative(self):
        nums = [0, 1, -1]
        k = 0
        rez = self.sol.subarraySum(nums, k)
        self.assertEqual(rez, 3)

    def test_small(self):
        nums = [1,2,3] 
        k = 3
        rez = self.sol.subarraySum(nums, k)
        self.assertEqual(rez, 2)

    def test_ones(self):
        nums = [1,1,1] 
        k = 1
        rez = self.sol.subarraySum(nums, k)
        self.assertEqual(rez, 3)

unittest.main()
