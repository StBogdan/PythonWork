from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumseen = defaultdict(int)
        cs = 0
        ans = 0
        for x in nums:
            cs += x
            if cs == k:
                ans += 1
            if cs - k in sumseen:
                ans += sumseen[cs-k]
            sumseen[cs] += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(str(sol.subarraySum([0, 1, -1], 0)) + " should be 3")
    print(str(sol.subarraySum([0, 1, -1], 1)) + " should be 2")
    print(str(sol.subarraySum([1, 1, 1], 2)) + " should be 2")
