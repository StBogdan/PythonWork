from collections import Counter

from typing import List

import math

import math


class Solution:
    def smallestDivisor(self, nums: List[int], t: int) -> int:
        lowbound = sum(int(num / t) for num in nums)
        highbound = max(nums)
        x = lowbound
        while lowbound <= highbound:
            if lowbound == highbound:
                return lowbound

            x = lowbound + int((highbound - lowbound) / 2)
            cur_sum = sum(math.ceil(num / x) for num in nums)

            if cur_sum > t:

                if x > lowbound:
                    lowbound = x
                else:
                    lowbound += 1
            else:
                if x == highbound:
                    return x
                highbound = x

        return x


if __name__ == '__main__':
    g, t = [962551,933661,905225,923035,990560], 10

    sol = Solution()
    print(sol.smallestDivisor(g, t))
