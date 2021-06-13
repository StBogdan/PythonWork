from typing import List

# Name: Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Method: Construct via recursion
# Time: O(4^n)
# Space: O(4^n)
# Difficulty: Medium


T9 = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str, idx=0):
        return self.letterCombinations_rec(digits, 0)

    def letterCombinations_rec(self, digits: str, idx=0) -> List[str]:
        digits_len = len(digits) - idx
        if len(digits) == idx:
            return []
        if digits_len == 1:
            return [x for x in T9[digits[idx]]]
        else:
            intermed = self.letterCombinations_rec(digits, idx + 1)
            return [ltr + rest for ltr in T9[digits[idx]] for rest in intermed]

    def letterCombinations_iter(self, digits: str, idx=0) -> List[str]:
        ans = set()
        for digit_str in digits:
            new_set = set()
            for ltr in T9[digit_str]:
                new_set.update({prev + ltr for prev in ans})
            ans = new_set
        return ans
