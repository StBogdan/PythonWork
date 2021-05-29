# Name: Strobogrammatic Number II
# Link: https://leetcode.com/problems/strobogrammatic-number-ii/
# Method: Build rotation out from core, lookout for zeroes
# Time: O(5^n)
# Space: O(5^n)
# Difficulty: Medium

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res_raw = self.find_strobogrammatic_rec(n)
        if n == 1:
            return self.find_strobogrammatic_rec(1)
        return [x for x in res_raw if x[0] != "0"]

    @staticmethod
    def find_strobogrammatic_rec(n: int) -> List[str]:
        rotations = (("6", "9"), ("8", "8"), ("1", "1"), ("9", "6"), ("0", "0"))
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        smaller_nums = Solution.find_strobogrammatic_rec(n - 2)
        all_sbmt_nr = []

        return (
            rot_start + sub_num + rot_end
            for sub_num in smaller_nums
            for rot_start, rot_end in rotations
        )
