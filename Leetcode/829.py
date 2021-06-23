# Name: Consecutive Numbers Sum
# Link: https://leetcode.com/problems/consecutive-numbers-sum/
# Method: Math, model seq as N = x + x + 1 + ... x + k, loop over values of k
# Time: O(N^(1/2))
# Space: O(1)
# Difficulty: Hard


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ways = 0
        i = 1
        while i * (i - 1) // 2 < N:
            current_result = N - i * (i - 1) // 2
            # print(current_result)
            if current_result % i == 0:
                ways += 1
            i += 1
        return ways


if __name__ == "__main__":
    exs = [5, 4, 9, 15]
    sol = Solution()
    for target in exs:
        print(f"Target {target} has ways: {sol.consecutiveNumbersSum(target)}")
