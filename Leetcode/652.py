from collections import defaultdict
from typing import List

# Name: Find Duplicate Subtrees
# Link: https://leetcode.com/problems/find-duplicate-subtrees/submissions/
# Method: Solving tidbit
# Time: O(n^2)
# Space: O(n^2)
# Difficulty: Medium


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        node_repr = defaultdict(list)

        def stringify_tree(node: TreeNode):
            if not node:
                return "null"

            left_res = stringify_tree(node.left)
            right_res = stringify_tree(node.right)
            res = f"{node.val},{left_res},{right_res}"
            node_repr[res].append(node)
            return res

        stringify_tree(root)
        return [
            tree_roots[0] for tree_roots in node_repr.values() if len(tree_roots) > 1
        ]
