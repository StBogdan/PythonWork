from typing import List
from collections import defaultdict

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        start_p = 0
        end_p = 0

        if not s:
            return 0

        key_map = defaultdict(int)
        key_map[s[0]] = 1
        c_max = s[0]

        while end_p < len(s) - 1:
            end_p += 1
            key_map[s[end_p]] += 1

            size_now = end_p - start_p + 1
            if size_now - key_map[c_max] > (size_now // 2):
                c_max, _ = max(key_map.items(), key=lambda ab: ab[1])

            is_valid = size_now - key_map[c_max] <= k

            # print(f"Between {start_p} and {end_p}, c_max {c_max} and counter {key_map}, is_valid {is_valid}")
            while not is_valid:
                key_map[s[start_p]] -= 1
                start_p += 1
                size_now = end_p - start_p + 1

                if size_now - key_map[c_max] > (size_now // 2):
                    c_max, _ = max(key_map.items(), key=lambda ab: ab[1])

                is_valid = size_now - key_map[c_max] <= k
                # print(f"Between {start_p} and {end_p}, c_max {c_max} and counter {key_map}, valid {is_valid}")

            longest = max(end_p - start_p + 1, longest)

        return longest


if __name__ == "__main__":
    exs = (("AAABBBFFB", 3), ("AAABBBFFB", 0), ("AAABBBFFB", 4), ("ABAB", 2))
    sol = Solution()

    for target, k in exs:
        print(f"For {target} and {k} we have {sol.characterReplacement(target,k)}")
        print("-" * 50)
