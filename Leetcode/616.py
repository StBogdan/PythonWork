from typing import Dict, List

# Name:  Add Bold Tag in String
# Link: https://leetcode.com/problems/add-bold-tag-in-string/
# Method: Trie and array of bolded indexes, check words starting at index
# Time: O(w + n*m)
# Space: O(w + n)
# Difficulty: Mediun
# Notes: w = characters in all words, m = longest word


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        return Solution.bolden_word(s, words)

    @staticmethod
    def words_to_trie(words: List[str]) -> Dict:
        trie = {}
        for word in words:
            trie_head = trie
            for ltr in word:
                trie_head = trie_head.setdefault(ltr, {})
            trie_head["_is_finish"] = True
        return trie

    @staticmethod
    def bolden_word(s: str, words: List[str]) -> str:
        is_bold = [False for _ in range(len(s))]
        trie = Solution.words_to_trie(words)
        for i in range(len(s)):
            Solution.bold_words_starting_at(i, s, trie, is_bold)

        res = ""
        i = 0
        while i < len(s):
            if is_bold[i]:
                res += "<b>"
                while i < len(s) and is_bold[i]:
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        return res

    @staticmethod
    def bold_words_starting_at(idx, s, trie, is_bold):
        start = idx
        trie_head = trie
        while idx < len(s) and s[idx] in trie_head:
            # print(f"Looking for {idx=} next={trie_head[s[idx]].keys()} ltrs: {s[idx]=}")
            if "_is_finish" in trie_head[s[idx]]:
                for j in range(start, idx + 1):
                    is_bold[j] = True
            trie_head = trie_head[s[idx]]
            idx += 1
