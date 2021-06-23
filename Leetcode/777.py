# Name: Swap Adjacent in LR String
# Link: https://leetcode.com/problems/swap-adjacent-in-lr-string/
# Method: Check relative positions of L, R
# Time: O(n)
# Space: O(n)
# Difficulty: Medium


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_poz = [(poz, elem) for poz, elem in enumerate(start) if elem != "X"]
        end_poz = [(poz, elem) for poz, elem in enumerate(end) if elem != "X"]
        if len(start_poz) != len(end_poz) or len(start) != len(end):
            return False
        for start_tpl, end_tpl in zip(start_poz, end_poz):
            start_idx, start_ltr = start_tpl
            end_idx, end_ltr = end_tpl
            if start_ltr != end_ltr:
                return False
            if (start_ltr == "L" and start_idx < end_idx) or (
                start_ltr == "R" and start_idx > end_idx
            ):
                return False
        return True
