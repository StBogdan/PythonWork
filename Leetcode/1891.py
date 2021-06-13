from typing import List

# Name: Cutting Ribbons
# Link: https://leetcode.com/problems/cutting-ribbons/
# Method: Binary search on the possible ribbon length
# Time: O(n*log(max(n)))
# Space: O(1)
# Difficulty: Medium


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        max_len = max(ribbons)
        min_len = 1
        best_ribbon_len = 0

        while min_len <= max_len:
            target_len = (max_len + min_len) // 2
            ribbon_nr = self.ribbons_cuttable_of_len(ribbons, target_len)

            if ribbon_nr >= k:
                best_ribbon_len = target_len
                min_len = target_len + 1
            else:
                max_len = target_len - 1

        return best_ribbon_len

    @staticmethod
    def ribbons_cuttable_of_len(ribs: List[int], target_len: int) -> int:
        return sum(rib // target_len for rib in ribs)
