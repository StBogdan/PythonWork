from typing import List

# Name: Number Of Rectangles That Can Form The Largest Square
# Link: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# Difficulty: Easy
# Method: Find max and count
# Time: O(n)
# Space: O(1)


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        for w, l in rectangles:
            max_len = max(max_len, min(w, l))

        max_occ = 0
        for w, l in rectangles:
            square_len = min(w, l)
            if square_len == max_len:
                max_occ += 1
        return max_occ


if __name__ == "__main__":
    exs = (
        [],
        [[5, 8], [3, 9], [5, 12], [16, 5]],
        [[2, 3], [3, 7], [4, 3], [3, 7]],
    )
    sol = Solution()
    for rect in exs:
        print(
            f"For input {rect}, found occurence of max len {sol.countGoodRectangles(rect)}"
        )
