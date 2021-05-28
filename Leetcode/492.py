# Name: License Key Formatting
# Link: https://leetcode.com/problems/license-key-formatting/
# Method: Build backwards string from letters
# Time: O(n)
# Space: O(n)
# Difficulty: Easy


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        rev_s = s.replace("-", "").upper()[::-1]
        reversed_ans = "-".join(rev_s[i : i + k] for i in range(0, len(rev_s), k))
        return reversed_ans[::-1]
