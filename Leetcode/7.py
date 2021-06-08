# Name: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/
# Method: Pop via mod, build new int
# Time: O(log(n))
# Space: O(1)
# Difficulty: Easy


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if (x < 0) else 1
        x = abs(x)
        new_nr = 0

        while x != 0:
            digit = x % 10
            new_nr = new_nr * 10 + digit

            x //= 10
            if new_nr > 2 ** 31:
                return 0

        return new_nr * sign
