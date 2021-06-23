# Name: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Method: DP, is string from [i,j] a palindrome (alternatively, expand from middle)
# Time: O(n^2)
# Space: O(n)
# Difficulty: Medium


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal_len = 1
        max_val_idx = [0, 0]

        # Optimised DP using only 2 lines
        is_pal_line = [False for _ in range(len(s))]
        is_pal_line[-1] = True

        for i in range(len(s) - 1, -1, -1):  # From bottom up, looking after diagonal
            is_pal_now = [False for _ in range(len(s))]
            is_pal_now[i] = True
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (j - i == 1 or is_pal_prev[j - 1]):
                    is_pal_now[j] = True
                    if j - i + 1 > max_pal_len:
                        max_pal_len = j - i + 1
                        max_val_idx = [i, j]
            is_pal_prev = is_pal_now

        return s[max_val_idx[0] : max_val_idx[1] + 1]
