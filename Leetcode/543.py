# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    
    cmax = 0
    
    def rec_dia(self, node):
        if not node:
            return 0

        depth_l = self.rec_dia(node.left) 
        depth_r = self.rec_dia(node.right)

        dia_at = depth_l + depth_r
        print(f"At node {node.val} diameter is {dia_at}") 
        if dia_at > self.cmax:
            self.cmax = dia_at
        
        return 1 + max(depth_l, depth_r)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
       self.cmax =0
       self.rec_dia(root)
       return self.cmax


if __name__ == "__main__":
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.left.left = TreeNode(3)

   root.right = TreeNode(4)

   root2 = TreeNode(0)
   root2.left = TreeNode(1)
   sol = Solution()
   # print(sol.diameterOfBinaryTree(root))
   print(sol.diameterOfBinaryTree(root2))
