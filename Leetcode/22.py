from itertools import lru_cache
from typing import List

# Name: Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/
# Method: Budget-based building, adding left and right parans
# Time: O(4^n / sqrt(n))
# Space: O(4^n / sqrt(n))
# Difficulty: Medium
# Notes: Something something n-th Catalan number, the LC solution has more details

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # print(self.paran_gen_closure(n))
        self.paran_gen("", n * 2, 0, ans)
        return ans
        # return self.paran_gen_closure(n)

    def paran_gen(self, parans: str, budget: int, lb: int, res=None) -> None:
        if not budget:
            if not lb:
                res.append(parans)
            return

        self.paran_gen(parans + "(", budget - 1, lb + 1, res)
        if lb > 0:
            self.paran_gen(parans + ")", budget - 1, lb - 1, res)

    @lru_cache
    def paran_gen_closure(self, pairs: int):
        if pairs == 0:
            return [""]
        if pairs == 1:
            return ["()"]

        options = set()
        for l_pairs in range(0, pairs):
            r_pairs = pairs - l_pairs - 1
            options.update(
                {
                    f"({l}){r}"
                    for l in self.paran_gen_closure(l_pairs)
                    for r in self.paran_gen_closure(r_pairs)
                }
            )

        return options
