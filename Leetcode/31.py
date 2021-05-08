from typing import List
import unittest

# Name: Next Permutation
# Link: https://leetcode.com/problems/next-permutation/
# Method: First end of decresing seq, swap end of that with first larger in the seq, reverse the rest
# Time: O(n)
# Space: O(1)
# Difficulty: Medium


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ind_now = n - 2
        while 0 <= ind_now and nums[ind_now] >= nums[ind_now+1]:
            ind_now -= 1

        if ind_now < 0:
            self.reverse_list(nums, 0, n - 1)
        else:
            swap_poz = ind_now
            swap_elem = nums[ind_now]

            ind_now += 1
            while ind_now < n-1 and nums[ind_now+1] > swap_elem:
                ind_now += 1

            nums[ind_now], nums[swap_poz] = nums[swap_poz], nums[ind_now]
            self.reverse_list(nums, swap_poz+1, n - 1)

    def reverse_list(self, nums, start, end):
        midpoint = (end - start + 1) // 2
        for i in range(midpoint):
            l = start + i
            r = end - i
            nums[l], nums[r] = nums[r], nums[l]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_lc1(self):
        res = [1, 3, 2]
        self.sol.nextPermutation(res)
        self.assertEqual(res, [2, 1, 3])

    def test_lc2(self):
        res = [1, 2, 3]
        self.sol.nextPermutation(res)
        self.assertEqual(res, [1, 3, 2])

    def test_lc3(self):
        res = [3, 2, 1]
        self.sol.nextPermutation(res)
        self.assertEqual(res, [1, 2, 3])

    def test_lc_short(self):
        res = [3]
        self.sol.nextPermutation(res)
        self.assertEqual(res, [3])

    def test_lc_long(self):
        res = [1, 5, 8, 4, 7, 6, 5, 3, 1]
        self.sol.nextPermutation(res)
        self.assertEqual(res, [1, 5, 8, 5, 1, 3, 4, 6, 7])


unittest.main()
