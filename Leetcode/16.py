from typing import List

# Name: 3Sum Closest
# Link: https://leetcode.com/problems/3sum-closest/
# Method: Like 3sum, but keep track of best candidate
# Time: O(n^2)
# Space: O(n)
# Difficulty: Medium


class Solution:
    def threeSumClosest_inital(self, nums: List[int], target: int) -> int:
        arr = sorted(nums)
        n = len(arr)

        current_dist = -1
        current_closest = -1
        for i in range(n):
            # 2sum with pointers
            left = 0
            right = n - 1
            ct = target - arr[i]

            while left < right:

                # Skip the element we are currently on
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                # Calc current elem, decide progess
                # print(f"Setting c2s as {arr[left]} and {arr[right]}")
                c2s = arr[left] + arr[right]
                if c2s > ct:
                    right -= 1
                elif c2s < ct:
                    left += 1
                else:
                    return target
                # print(f"Got intermediary for {i}, dist {abs(ct - c2s)} on target {ct} and c2s {c2s}")
                if current_dist > 0:
                    if abs(ct - c2s) < current_dist:
                        current_dist = abs(c2s - ct)
                        current_closest = c2s + arr[i]
                        # print(f"Set sum to {current_closest} as dist is {current_dist}")
                else:  # Initial call
                    current_dist = abs(c2s - ct)
                    current_closest = c2s + arr[i]
                    # print(f"Set sum to {current_closest} as dist is {current_dist}")
        return current_closest

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        arr = sorted(nums)
        n = len(arr)
        current_dist = -1
        current_closest = -1
        for i in range(n):
            # 2sum with pointers
            left = 0
            right = n - 1

            while left < i < right:
                twosum_curr = arr[left] + arr[i] + arr[right]
                if twosum_curr > target:
                    right -= 1
                elif twosum_curr < target:
                    left += 1
                else:
                    return target

                if current_dist > 0:
                    if abs(target - twosum_curr) < current_dist:
                        current_dist = abs(twosum_curr - target)
                        current_closest = twosum_curr
                else:  # Initial call
                    current_dist = abs(twosum_curr - target)
                    current_closest = twosum_curr
        return current_closest


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    t = 1

    sol = Solution()
    assert 2 == sol.threeSumClosest(nums, t)

    nums2 = [1, 2, 3]
    t2 = 0
    assert 6 == sol.threeSumClosest(nums2, t2)

    nums3 = [1, 6, 9, 14, 16, 70]
    t3 = 81
    assert 80 == sol.threeSumClosest(nums3, t3)
