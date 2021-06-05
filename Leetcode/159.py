from collections import defaultdict

# Name: Longest Substring with At Most Two Distinct Characters
# Link: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# Method: Sliding window with char counter
# Time: O(n)
# Space: O(1)
# Difficulty: Medium


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        count = defaultdict(int, {s[0]: 1})
        start_idx = 0
        len_max = 1
        for i in range(1, len(s)):
            count[s[i]] += 1
            while len(count) >= 3 and start_idx <= i:
                count[s[start_idx]] -= 1
                if count[s[start_idx]] == 0:
                    del count[s[start_idx]]
                start_idx += 1
            len_max = max(i - start_idx + 1, len_max)
        return len_max