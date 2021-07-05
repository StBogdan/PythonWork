from typing import List

# Name: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# Link: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
# Method: Max vert interval, max horiz interval
# Time: O(n\*log(n))
# Space: O(n)
# Difficulty: Medium


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        max_h_cut = h - horizontalCuts[-1]
        max_v_cut = w - verticalCuts[-1]

        for h_idx in range(len(horizontalCuts)):
            prev = horizontalCuts[h_idx - 1] if h_idx > 0 else 0
            max_h_cut = max(horizontalCuts[h_idx] - prev, max_h_cut)

        for v_idx in range(len(verticalCuts)):
            prev = verticalCuts[v_idx - 1] if v_idx > 0 else 0
            max_v_cut = max(verticalCuts[v_idx] - prev, max_v_cut)

        return max_h_cut * max_v_cut % (10 ** 9 + 7)
