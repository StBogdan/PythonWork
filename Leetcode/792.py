from typing import DefaultDict, List

# Name: Number of Matching Subsequences
# Link: https://leetcode.com/problems/number-of-matching-subsequences/
# Method: Buckets with next letter pointer
# Time: O(n * m)
# Space: O(m)
# Difficulty: Medium
# Note: m = nr of words

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_pointers = DefaultDict(list)
        for idx, word in enumerate(words):
            word_pointers[word[0]].append((idx, 0))
        found_words = 0

        for ltr in s:
            match_list = word_pointers[ltr][:]
            word_pointers[ltr] = []
            for match_idx, word_idx in match_list:
                new_word_idx = word_idx + 1

                if new_word_idx == len(words[match_idx]):
                    found_words += 1
                else:
                    next_word_ltr = words[match_idx][new_word_idx]
                    word_pointers[next_word_ltr].append((match_idx, new_word_idx))
        return found_words
