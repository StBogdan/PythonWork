from typing import List
import unittest


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(1, self.sol.missingNumber([0]))

    def test_small(self):
        self.assertEqual(2, self.sol.missingNumber([0, 1, 3, 4]))

    def test_big(self):
        self.assertEqual(8, self.sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


unittest.main()
