from typing import List

# Name: Problem name
# Link: https://leetcode.com/problems/problem-name
# Method: Solving tidbit
# Time: O(1)
# Space: O(1)
# Difficulty: чики-брики


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.left) + "/" + str(self.val) + "\\" + str(self.right)


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        node_now = root
        for i in range(1, len(preorder)):
            print(f"Placing {preorder[i]}")
            if preorder[i] < node_now.val:
                node_now.left = TreeNode(preorder[i])
                node_now.left.parent = node_now
                node_now = node_now.left
            else:
                print(f"{preorder[i]} bigger than val: {node_now.val}")
                pcan = node_now
                while node_now.parent and node_now.parent.val < preorder[i]:
                    print(f"Going up to cn.parent {node_now.parent.val}")
                    if node_now.parent.right == None:
                        pcan = node_now.parent
                    node_now = node_now.parent
                print(f"At pcan: {pcan.val}")
                pcan.right = TreeNode(preorder[i])
                pcan.right.parent = pcan
                node_now = pcan.right

        return root


if __name__ == "__main__":
    sol = Solution()
    inp = [8, 5, 1, 7, 10, 12]
    print(sol.bstFromPreorder(inp))
