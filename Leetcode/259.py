import unittest
from typing import List

# Method: 3sum, but count moving right down when below limit
# Time: O(n^2)
# Space: O(n)


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        snums = sorted(nums)
        triples = 0
        for i in range(len(snums)-2):

            l = i+1
            r = len(snums) - 1

            while l < r:
                csum = snums[i] + snums[l] + snums[r]
                if csum < target:
                    triples += r - l
                    l += 1
                else:
                    r -= 1

        return triples


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        arr = []
        target = 3
        self.assertEqual(self.sol.threeSumSmaller(arr, target), 0)

    def test_less_than_3(self):
        arr = [1, 2]
        target = 3
        self.assertEqual(self.sol.threeSumSmaller(arr, target), 0)

    def test_small(self):
        arr = [-2, 0, 1, 3]
        target = 2
        self.assertEqual(self.sol.threeSumSmaller(arr, target), 2)

    def test_bigger(self):
        arr = [6, 5, 7, 10, 23, 5, 6, 7, 8, 49, 10, 3, 5]
        target = 21
        self.assertEqual(self.sol.threeSumSmaller(arr, target), 99)


unittest.main()
