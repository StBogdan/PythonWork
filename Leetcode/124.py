

# Method: Recursive, get maximum path with a node in it, feed up (check max if going down again)
# Time: O(n)
# Space: O(d) where d = tree depth (worst case also n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = root.val
        
        def max_path_containing(node: TreeNode):
            if not node:
                return 0
            
            left_max = max(max_path_containing(node.left), 0)
            right_max = max(max_path_containing(node.right),0)
            branch_max = max(left_max,right_max)
            
            self.max_path = max(self.max_path, node.val + left_max + right_max)
            return node.val + branch_max
        
        max_path_containing(root)
        
        return self.max_path
