from collections import Counter


# Name: Number of Good Ways to Split a String
# Link: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# Method: Counter of occurences for start and end
# Time: O(n)
# Space: O(n)
# Difficulty: Medium


class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0

        counter_curr = Counter()
        uniq_curr = 0

        counter_rest = Counter(s)
        uniq_rest = len(counter_rest)

        good_cuts = 0

        for ltr in s:
            counter_rest[ltr] -= 1
            if counter_rest[ltr] == 0:
                uniq_rest -= 1

            if ltr not in counter_curr:
                uniq_curr += 1
            counter_curr[ltr] += 1

            if uniq_curr == uniq_rest:
                good_cuts += 1
        return good_cuts

    def numSplits_compressed(self, s: str) -> int:
        """Less lines, uses set"""
        if len(s) < 2:
            return 0

        counter_curr = set()
        counter_rest = Counter(s)
        good_cuts = 0

        for ltr in s:
            counter_rest[ltr] -= 1
            if not counter_rest[ltr]:
                del counter_rest[ltr]
            counter_curr.add(ltr)
            good_cuts += len(counter_rest) == len(counter_curr)
        return good_cuts
