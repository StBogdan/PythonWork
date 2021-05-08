from typing import List
import unittest

# Name: Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Method: Sort and pairwise compare
# Time: O(n*log(n))
# Space: O(n) Result array
# Difficulty: Medium


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals

        sorted_interv = list(sorted(intervals, key=lambda x: x[0]))
        # For each conseq pair, see if merge-able, if not, put prev in ans arr
        span_now = sorted_interv[0]

        ans = []
        for i in range(1, len(intervals)):
            start, end = sorted_interv[i]
            if start <= span_now[1]:
                span_now[1] = max(span_now[1], end)
            else:
                ans.append(span_now)
                span_now = sorted_interv[i]

        ans.append(span_now)

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_one_interval(self):
        res = self.sol.merge([[1, 4]])
        self.assertEqual(res, [[1, 4]])

    def test_exact_overlap(self):
        res = self.sol.merge([[1, 4], [4, 10], [10, 20]])
        self.assertEqual(res, [[1, 20]])

    def test_lc1(self):
        res = self.sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        self.assertEqual(res, [[1, 6], [8, 10], [15, 18]])

    def test_lc2(self):
        res = self.sol.merge([[1, 4], [4, 5]])
        self.assertEqual(res, [[1, 5]])


unittest.main()
