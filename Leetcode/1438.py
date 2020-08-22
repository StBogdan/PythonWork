from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()

        len_max = 0
        r = 0
        l = 0
        while r < len(nums):
            while min_dq and nums[r] <= nums[min_dq[-1]]:
                min_dq.pop()

            while max_dq and nums[r] >= nums[max_dq[-1]]:
                max_dq.pop()

            min_dq.append(r)
            max_dq.append(r)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                l += 1
                if l > min_dq[0]:
                    min_dq.popleft()

                if l > max_dq[0]:
                    max_dq.popleft()

            len_max = max(len_max, r - l + 1)
            r += 1
        return len_max


if __name__ == "__main__":
    exs = [([10, 1, 2, 4, 7, 2], 5)]
    sol = Solution()

    for arr, t in exs:
        print(f"Longest subarr is {sol.longestSubarray(arr, t)}")
