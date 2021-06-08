from typing import List, Set

# Name: Delete Nodes And Return Forest
# Link: https://leetcode.com/problems/delete-nodes-and-return-forest/
# Method: Recursive, passing down flag for the possiblity of being root
# Time: O(n)
# Space: O(n)
# Difficulty: Medium


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        roots = []
        deletions = set(to_delete)

        def del_nodes_rec(
            node: TreeNode,
            is_root: bool,
        ) -> None:
            marked_for_deletion = node.val in deletions
            if is_root and not marked_for_deletion:
                roots.append(node)

            if node.left:
                target = node.left
                if target.val in deletions:
                    node.left = None
                del_nodes_rec(target, marked_for_deletion)

            if node.right:
                target = node.right
                if target.val in deletions:
                    node.right = None
                del_nodes_rec(target, marked_for_deletion)

        del_nodes_rec(root, True)
        return roots
