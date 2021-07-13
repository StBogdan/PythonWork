from typing import Deque, List

# Name: Number of Provinces
# Link: https://leetcode.com/problems/number-of-provinces/
# Method: BFS, DFS, graph traversal connected components
# Time: O(n^2)
# Space: O(n)
# Difficulty: Medium

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
      visited = set()
      provinces = 0
      for i in range(len(isConnected)):
        if i in visited:
          continue
        
        provinces +=1
        to_visit = Deque()
        to_visit.append(i)
        
        while to_visit:
          node_now = to_visit.popleft()
          visited.add(node_now)
          
          for vecin in range(len(isConnected)):
            if isConnected[node_now][vecin] and vecin not in visited:
              to_visit.append(vecin)
              
      return provinces
          