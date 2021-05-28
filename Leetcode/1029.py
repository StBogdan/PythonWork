from typing import List

# Name: Two City Scheduling
# Link: https://leetcode.com/problems/two-city-scheduling/
# Method: Relative difference sorting
# Time: O(n * log(n))
# Space: O(n)
# Difficulty: Medium


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        sorted_costs = sorted(costs, key=lambda x: x[1] - x[0])

        return sum(sorted_costs[i][1] + sorted_costs[n + i][0] for i in range(n))

        # return sum(x[0] if i >= len(costs)//2 else x[1] \
        #            for i, x in enumerate(sorted(costs, key=lambda x: x[1] - x[0])))
