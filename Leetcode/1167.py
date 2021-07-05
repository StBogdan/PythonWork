import heapq
from typing import List

# Name: Minimum Cost to Connect Sticks
# Link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# Method: MinHeap, construct sum
# Time: O(n\*log(n))
# Space: O(n)
# Difficulty: Medium


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        sum_now = 0
        while len(sticks) > 1:
            min_1, min_2 = heapq.heappop(sticks), heapq.heappop(sticks)
            new_elem = min_1 + min_2
            sum_now += new_elem
            heapq.heappush(sticks, new_elem)
        return sum_now
