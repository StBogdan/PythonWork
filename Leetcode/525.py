from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        seen_balls = {0: -1}  # Cover the case where all array is balanced
        cmax = 0
        bal = 0
        for i in range(n):

            bal += 2*nums[i] - 1
            if bal in seen_balls:
                cmax = max(cmax, i - seen_balls[bal])
            else:
                seen_balls[bal] = i
        return cmax


if __name__ == "__main__":
    sol = Solution()
    n1 = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0]

    print(sol.findMaxLength(n1))
