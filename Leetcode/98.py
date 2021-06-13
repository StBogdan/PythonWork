from typing import Optional

# Name: Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Method: Recursion, with edge case checking
# Time: O(n)
# Space: O(depth)
# Difficulty: Medium


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return bool(self.sub_bst_edges(root))

    def sub_bst_edges(self, root: TreeNode) -> Optional[tuple]:
        if not root:
            return None

        left = self.sub_bst_edges(root.left)
        right = self.sub_bst_edges(root.right)

        if (
            (not left and root.left is not None)
            or (not right and root.right is not None)
            or (root.left and root.val <= left[1])
            or (root.right and root.val >= right[0])
        ):
            return None

        return (
            left[0] if root.left else root.val,
            right[1] if root.right else root.val,
        )
