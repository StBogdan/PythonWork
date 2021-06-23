# Name: Sentence Screen Fitting
# Link: https://leetcode.com/problems/sentence-screen-fitting/
# Method: DP, store the word starting the next row, if starting this row with word i
# Time: O(~r \* c )
# Space: O(w)
# Difficulty: Medium
# Note: w = nr of words in sentence


from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        c_word = 0
        finished = 0
        word_lens = [len(s) for s in sentence]
        memo = {}
        for row in range(rows):
            if c_word in memo:
                c_word, finished_on_row = memo[c_word]
                finished += finished_on_row
                continue

            col_budget = cols
            finished_now = 0
            starting_word = c_word
            while col_budget >= word_lens[c_word]:
                col_budget -= word_lens[c_word] + 1
                c_word += 1
                if c_word == len(sentence):
                    c_word = 0
                    finished_now += 1
            finished += finished_now
            memo[starting_word] = (c_word, finished_now)
        return finished
