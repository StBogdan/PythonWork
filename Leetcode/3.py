import unittest

# Method: 2 pointers, sliding window and a set
# Time: O(n)
# Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        len_max = 1
        elem_seen = set()
        start = 0
        for i, ltr in enumerate(s):
            if ltr in elem_seen:
                len_max = max(i- start, len_max)
                while start < i and ltr in elem_seen:
                    elem_seen.remove(s[start])
                    start += 1
            elem_seen.add(ltr)

        len_max = max(len(s)- start, len_max)
        return len_max


class TestLongestNoRepeats(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_lc_1(self):
        res = self.sol.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(res, 3)

    def test_lc_2(self):
        res = self.sol.lengthOfLongestSubstring("bbbb")
        self.assertEqual(res, 1)

    def test_lc_3(self):
        res = self.sol.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(res, 3)

    def test_re_appear(self):
        res = self.sol.lengthOfLongestSubstring("abcdbefzghij")
        self.assertEqual(res, 10)
    
    def test_all_uniq(self):
        res = self.sol.lengthOfLongestSubstring("abcd")
        self.assertEqual(res, 4)

unittest.main()
