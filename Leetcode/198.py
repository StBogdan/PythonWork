from typing import List

# Name: House Robber
# Link: https://leetcode.com/problems/house-robber/
# Method: Dynamic programming, max of prev 2 days
# Time: O(n)
# Space: O(1)
# Difficulty: Medium

class Solution:
    def rob(self, nums:List[int]) -> int:
        rob_prev = 0
        rob_max = 0
        for x in nums:
            temp = rob_max
            rob_max = max(rob_prev + x, rob_max)
            rob_prev= temp
        return rob_max
    
    
    def rob_alternate(self, nums: List[int]) -> int:
        prev_houses = [0,0,0]
        
        for i in range(len(nums)):
            stolen_now = max(prev_houses[1], prev_houses[0]) + nums[i]
            prev_houses[0] = prev_houses[1] 
            prev_houses[1] = prev_houses[2] 
            prev_houses[2] = stolen_now
        
        print(prev_houses)
        return max(prev_houses)