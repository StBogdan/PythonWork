from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if not nums:
            return -1

        l = 0
        h = n
        pivot = 0
        while l < h:
            mid = (l + h) // 2
            x = nums[mid]

            if mid + 1 < n and x > nums[mid + 1]:
                pivot = mid + 1
                break
            elif mid > 1 and x < nums[mid - 1]:
                pivot = mid
                break
            elif x > nums[0]:
                l = mid + 1
            elif x < nums[-1]:
                h = mid
            else:
                print(f"Oh no, in case l: {l} h:{h} mid:{mid}")
                pivot = 1
                break

        print(f"Pivot at {pivot}")

        l = 0
        h = n
        while l <= h:
            mid = (l + h) // 2
            i = (mid + pivot) % n
            x = nums[i]

            if x == target:
                return i
            elif x < target:
                l = mid + 1
            elif x > target:
                h = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()

    inp = [4, 5, 6, 7, 0, 1, 2]
    t = 10

    print(sol.search(inp, t))

    inp = [4, 5]
    t = 5

    print(f"{sol.search(inp, t)} is 1")

    inp = [4, 5]
    t = 4
    print(f"{sol.search(inp, t)} is 0")

    intp = [5, 4]
    t = 5
    print(f"{sol.search(inp, t)} is 0")
