from collections import defaultdict, deque
from typing import List

# Name: Vertical Order Traversal of a Binary Tree
# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Method: Traverse graph, store seen in a per-column dict, build output from dict
# Time: O(n * log(n))
# Space: O(n)
# Difficulty: Hard


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        cols = defaultdict(lambda: defaultdict(list))
        min_col, max_col = 0, 0

        queue = deque()
        queue.append((root, 0, 0))
        while queue:  # BFS traversal
            node, row, col = queue.popleft()

            # Keep track of width
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            cols[col][row].append(node.val)
            print(
                f"Looking at val {node.val=} at {row=} {col=}, "
                f"now know of {cols[col]}"
            )

            # Add children
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        ans = []
        for col in range(min_col, max_col + 1):
            col_vals = []
            for row_list in cols[col].values():
                col_vals += sorted(row_list)
            ans.append(col_vals)

        return ans
