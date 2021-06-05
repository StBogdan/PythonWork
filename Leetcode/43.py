# Name: Multiply Strings
# Link: https://leetcode.com/problems/multiply-strings/
# Method: Result array, see every digit pair (w/ pow(10) as offset in result)
# Time: O(n\*m)
# Space: O(n + m)
# Difficulty: Medium


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0 for _ in range(n1 + n2)]

        poz_offset = 0
        for digit1_idx in range(n1 - 1, -1, -1):
            digit1 = ord(num1[digit1_idx]) - ord("0")
            for digit2_idx in range(len(num2) - 1, -1, -1):
                digit2 = ord(num2[digit2_idx]) - ord("0")
                target_res_idx = n2 - 1 - digit2_idx + poz_offset

                res[target_res_idx] += digit1 * digit2
                res[target_res_idx + 1] += res[target_res_idx] // 10
                res[target_res_idx] %= 10
            poz_offset += 1

        rev_res = []
        stripped_zeroes = False
        for x in res[::-1]:
            if x != 0:
                stripped_zeroes = True
            if stripped_zeroes:
                rev_res.append(str(x))
        return "".join(rev_res)


