from math import sqrt
from typing import List


class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        smolest_diff = num*2
        smolest_vals = []

        targets = [num + 1, num + 2]
        for target in targets:
            for i in range(int(sqrt(target)+1), 0, -1):
                if not target % i:
                    j = target // i
                    if abs(i - j) < smolest_diff:
                        smolest_diff = abs(i - j)
                        smolest_vals = [i, j]

        print(smolest_vals)
        return smolest_vals


if __name__ == '__main__':
    sol = Solution()

    assert [5, 25] == sol.closestDivisors(123)
    assert {40, 25} == set(sol.closestDivisors(999))
    assert {1, 2} == set(sol.closestDivisors(1))
    assert {3, 3} == set(sol.closestDivisors(8))
    assert {4, 4} == set(sol.closestDivisors(15))
    assert {2409, 285773} == set(sol.closestDivisors(688427155))