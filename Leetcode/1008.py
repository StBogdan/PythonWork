from typing import List


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
        cn = root
        for i in range(1, len(preorder)):
            print(f"Placing {preorder[i]}")
            if preorder[i] < cn.val:
                cn.left = TreeNode(preorder[i])
                cn.left.parent = cn
                cn = cn.left
            else:
                print(f"{preorder[i]} bigger than val: {cn.val}")
                pcan = cn
                while cn.parent and cn.parent.val < preorder[i]:
                    print(f"Going up to cn.parent {cn.parent.val}")
                    if cn.parent.right == None:
                        pcan = cn.parent
                    cn = cn.parent
                print(f"At pcan: {pcan.val}")
                pcan.right = TreeNode(preorder[i])
                pcan.right.parent = pcan
                cn = pcan.right

        return root


if __name__ == "__main__":
    sol = Solution()
    inp = [8, 5, 1, 7, 10, 12]
    print(sol.bstFromPreorder(inp))
