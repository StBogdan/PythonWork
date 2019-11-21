from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        elif sum(nums) == s:
            return len(nums)

        start = 0
        end = 0
        c_sum = 0
        cmsa = len(nums) + 1

        while end < len(nums):
            c_sum += nums[end]

            while c_sum - nums[start] >= s and start <= end:
                c_sum -= nums[start]
                start += 1

            if (c_sum >= s):
                cmsa = min(cmsa, end - start + 1)
            end += 1
        return cmsa


if __name__ == '__main__':
    folder = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    print(f"Ans: {sol.minSubArrayLen(7, folder)}")
