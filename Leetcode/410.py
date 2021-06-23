from typing import List

# Name: Split Array Largest Sum
# Link: https://leetcode.com/problems/split-array-largest-sum
# Method: Dynamic programming, keep track of dp[partitions][to index] (alternatively, greedy binary search)
# Time: O(n^2 \* m)
# Space: O(n \* m)
# Difficulty: Hard


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        memo = {}
        return self.get_smaller_part_dp(nums, m)

    @staticmethod
    def get_smaller_part_dp(arr: List[int], m: int):
        n = len(arr)

        # Memo matrix, w/ padding
        dp = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = 0

        # Prefix sums
        sum_to = [0]
        for i in range(n):
            sum_to.append(sum_to[-1] + arr[i])

        for parts in range(1, m + 1):
            for poz in range(1, len(arr) + 1):
                for prev_poz in range(poz - 1, -1, -1):
                    current_sum = sum_to[poz] - sum_to[prev_poz]
                    dp[parts][poz] = min(
                        dp[parts][poz],
                        max(dp[parts - 1][prev_poz], current_sum),
                    )

                    if current_sum > dp[parts - 1][prev_poz]:
                        break

        for line in dp:
            print([f"{x:4}" for x in line])
        return dp[-1][-1]

    @staticmethod
    def get_smaller_part_brute_force(arr: List[int], start: int, parts: int, memo):
        if (start, parts) in memo:
            return memo[(start, parts)]

        n = len(arr)
        if parts == n - start:
            # print(f"Best rez for {start=} {parts=} is {max(arr[start:])}")
            return max(arr[start:])
        elif parts == 1:
            # print(f"Best rez for {start=} {parts=} is {sum(arr[start:])}")
            return sum(arr[start:])

        current_part_sum = 0
        best_min = float("inf")
        for start_point in range(start, n - parts + 1):
            current_part_sum += arr[start_point]
            min_of_rest_part = Solution.get_smaller_part(
                arr, start_point + 1, parts - 1, memo
            )
            best_min = min(best_min, max(current_part_sum, min_of_rest_part))

        memo[(start, parts)] = best_min
        # print(f"Best rez for {start=} {parts=} is {best_min=}")
        return best_min
