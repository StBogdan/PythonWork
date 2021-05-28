import unittest

# Name: Palindromic Substrings
# Link: https://leetcode.com/problems/palindromic-substrings/
# Method: Expand around centre (dp alternative included)
# Time: O(n^2)
# Space: O(1)
# Difficulty: Medium


class Solution:
    def countSubstrings_dp(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(s)):
            dp[i][i] = 1

        palindromes = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (i + 2 > j or dp[i + 1][j - 1])
                palindromes += dp[i][j]

        return palindromes

    def countSubstrings(self, s: str) -> int:
        return sum(
            self.palindrome_count_around(s, i, i)
            + self.palindrome_count_around(s, i, i + 1)
            for i in range(len(s))
        )

    @staticmethod
    def palindrome_count_around(s: str, low: int, high: int):
        ans = 0
        while 0 <= low and high < len(s):
            if s[low] != s[high]:
                break
            ans += 1
            low -= 1
            high += 1
        return ans


class TestPalindromeCount(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_letter(self):
        s = "a"
        expected_ans = 1
        self.assertEqual(self.sol.countSubstrings(s), expected_ans)
        self.assertEqual(self.sol.countSubstrings_dp(s), expected_ans)

    def test_lc_example(self):
        s = "aaa"
        expected_ans = 6
        self.assertEqual(self.sol.countSubstrings(s), expected_ans)
        self.assertEqual(self.sol.countSubstrings_dp(s), expected_ans)

    def test_longer(self):
        s = "afcfafcfadamedane"
        expected_ans = 26
        self.assertEqual(self.sol.countSubstrings(s), expected_ans)
        self.assertEqual(self.sol.countSubstrings_dp(s), expected_ans)


unittest.main()
