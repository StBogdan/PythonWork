# Name: Find And Replace in String
# Link: https://leetcode.com/problems/find-and-replace-in-string/
# Method: Construct parallel string, have lookup for indexes
# Time: O(n)
# Space: O(n)
# Difficulty: Medium


from typing import List


class Solution:
    def findReplaceString(
        self, s: str, indexes: List[int], sources: List[str], targets: List[str]
    ) -> str:
        subst_dict = {indexes[x]: (sources[x], targets[x]) for x in range(len(indexes))}
        res_string = ""
        read_index = 0
        while read_index < len(s):
            if read_index in subst_dict and self.source_match(
                s, read_index, subst_dict[read_index][0]
            ):
                source, target = subst_dict[read_index]
                res_string += target
                read_index += len(source)
            else:
                res_string += s[read_index]
                read_index += 1
        return res_string

    @staticmethod
    def source_match(src: str, start_idx: int, target: str) -> bool:
        return src[start_idx : start_idx + len(target)] == target
