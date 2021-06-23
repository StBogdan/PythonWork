# Name: Strobogrammatic Number
# Link: https://leetcode.com/problems/strobogrammatic-number/
# Method: Check if rotation is the same, work from both ends
# Time: O(n)
# Space: O(1)
# Difficulty: Easy


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotations = {"6": "9", "8": "8", "1": "1", "9": "6", "0": "0"}
        l, r = 0, len(num) - 1
        while l <= r:
            digit_l = num[l]
            digit_r = num[r]
            if digit_l not in rotations or rotations[digit_l] != digit_r:
                return False
            l += 1
            r -= 1
        return True
