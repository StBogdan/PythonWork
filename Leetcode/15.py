from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_arr = sorted(nums)
        n = len(sorted_arr)
        combos = set()
        for i in range(n):
            # 2sum with pointers
            left = 0
            right = n - 1

            while left < i < right:
                sum_now = sorted_arr[left] + sorted_arr[i] + sorted_arr[right]
                if sum_now > 0:
                    right -= 1
                elif sum_now < 0:
                    left += 1
                else:
                    combos.add((sorted_arr[left], sorted_arr[i], sorted_arr[right]))
                    left += 1

        return [list(tpl) for tpl in combos]


if __name__ == "__main__":
    nums1 = [-1, 0, 1, 2, -1, -4]
    ans1 = [[-1, 0, 1], [-1, -1, 2]]

    nums2 = [3, 0, -2, -1, 1, 2]

    sol = Solution()
    print(sol.threeSum(nums2))
