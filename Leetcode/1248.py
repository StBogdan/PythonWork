from typing import List

# Method: Sliding window with special reduction (maintain ways to build sub-arr)
# Time: O(n)
# Space: O(1)


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds_now = 0
        start = 0

        total_nice = 0
        ways = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odds_now += 1
                ways = 0

            while odds_now == k and start <= i:
                odds_now -= nums[start] % 2
                start += 1
                ways += 1

            total_nice += ways

        return total_nice

if __name__ == "__main__":
    exs = [
        ([1,1,2,1,1], 3),
        ([2,4,6], 1),
        ([2,2,2,1,2,2,1,2,2,2],2)
    ]
    sol = Solution()
    for arr, k in exs:
        res = sol.numberOfSubarrays(arr, k)
        print(f"Res: {res:4} for k: {k:2} and arr: {arr}")
