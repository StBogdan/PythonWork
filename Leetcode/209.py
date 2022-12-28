from typing import List

# Name: Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Method: Sliding window, once target sum is passed, reduce from left side as much as possible
# Time: O(n)
# Space: O(1)
# Difficulty: Medium

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)

        start = 0
        end = 0
        sum_now = 0
        min_size_now = len(nums) + 1

        while end < len(nums):
            sum_now += nums[end]

            while sum_now - nums[start] >= target and start <= end:
                sum_now -= nums[start]
                start += 1

            if sum_now >= target:
                min_size_now = min(min_size_now, end - start + 1)
            end += 1
        return min_size_now


if __name__ == "__main__":
    folder = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    print(f"Ans: {sol.minSubArrayLen(7, folder)}")
