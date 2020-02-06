from collections import Counter  # Strike
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        cdict = Counter(nums)

        vals = sorted(cdict.keys())
        print(vals)
        for x in range(len(vals) - k + 1):
            i = vals[x]
            print(f"Now at {x} of val {i}")
            if cdict[i] == 0:
                cdict.pop(i)
                pass  # No care
            elif cdict[i] < 0:
                return False  # Welp
            else:
                to_ss = cdict[i]
                cdict.pop(i)
                for j in range(i + 1, i + k):
                    print(f"Subs {j} {to_ss}")
                    if j not in cdict:
                        return False  # Required consecutive key not found
                    cdict[j] -= to_ss  # Reduce required for segmentation

        print(f"{cdict} and {all(v == 0 for v in cdict.values())}")
        return all(v == 0 for v in cdict.values())


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 6, 7, 8, 9, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 12, 13, 14, 15, 19]
    k = 5

    nums2 = [1, 2, 3, 3, 4, 4, 5, 6]
    k2 = 4

    nums3 = [1, 2, 3, 3, 4, 4, 5, 6]
    k3 = 4

    nums4 = [9, 13, 15, 23, 22, 25, 4, 4, 29, 15, 8, 23, 12, 19, 24, 17, 18, 11, 22, 24, 17, 17, 10, 23, 21, 18, 14, 18,
             7, 6, 3, 6, 19, 11, 16, 11, 12, 13, 8, 26, 17, 20, 13, 19, 22, 21, 27, 9, 20, 15, 20, 27, 8, 13, 25, 23,
             22, 15, 9, 14, 20, 10, 6, 5, 14, 12, 7, 16, 21, 18, 21, 24, 23, 10, 21, 16, 18, 16, 18, 5, 20, 19, 20, 10,
             14, 26, 2, 9, 19, 12, 28, 17, 5, 7, 25, 22, 16, 17, 21, 11]
    k4 = 10
    print(sol.isPossibleDivide(nums4, k4))
