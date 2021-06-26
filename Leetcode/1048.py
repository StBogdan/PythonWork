from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def are_in_order(short: str, long: str) -> bool:
        if len(short) > len(long):
            short, long = long, short

        if len(short) + 1 != len(long):
            return False

        idx = 0
        has_miss = 0
        while idx < len(short):
            if short[idx] != long[idx + has_miss]:
                if not has_miss:
                    has_miss = 1
                    continue
                else:
                    return False
            idx += 1
        return True

    def longestStrChain(self, words: List[str]) -> int:
        buckets = defaultdict(list)
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
            buckets[len(word)].append((word, 1))

        max_chain = 1
        for i in range(1, max_len + 1):
            words_of_len = buckets[i]
            for word_idx in range(len(words_of_len)):
                word, longest_chain = words_of_len[word_idx]
                for prev_word, prev_chain in buckets[i - 1]:
                    if self.are_in_order(prev_word, word):
                        longest_chain = max(longest_chain, prev_chain + 1)

                words_of_len[word_idx] = (word, longest_chain)
                max_chain = max(max_chain, longest_chain)

        return max_chain
