from typing import List

import heapq

# Name: Max Value of Equation
# Link: https://leetcode.com/problems/max-value-of-equation/
# Method: Decompose equation, max heap of prev (better with a monotonic queue)
# Time: O(n\*log(n))
# Space: O(n)
# Difficulty: Hard


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_eq_val = -float("inf")
        min_heap = []
        # Onto heap: ( - (-x + j), x), extra minus as default is min heap
        for x, y in points:
            while min_heap and min_heap[0][1] < x - k:
                heapq.heappop(min_heap)

            if min_heap:
                eq_res_now = -min_heap[0][0] + x + y
                max_eq_val = max(max_eq_val, eq_res_now)
            heapq.heappush(min_heap, (-(-x + y), x))

        return max_eq_val
