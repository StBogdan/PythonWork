from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        n = len(arr)
        combos = set()
        for i in range(n):
            # 2sum with pointers
            left = 0
            right = n - 1

            while left < i < right:
                c2s = arr[left] + arr[i] + arr[right]
                if c2s > 0:
                    right -= 1
                elif c2s < 0:
                    left += 1
                else:
                    combos.add((arr[left], arr[i], arr[right]))
                    left += 1

        return [list(tpl) for tpl in combos]


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    ans1 = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]

    nums2 = [3, 0, -2, -1, 1, 2]

    sol = Solution()
    print(sol.threeSum(nums2))
