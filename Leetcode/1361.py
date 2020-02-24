from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited_nodes = [0 for _ in range(n)]
        bin_trees = set()

        for i in range(n):
            if visited_nodes[i]:
                continue

            visited_nodes[i] = 1
            tovisit = [leftChild[i], rightChild[i]]
            while tovisit:
                cur_node = tovisit.pop()
                print(f"Now on node {cur_node} ---- {tovisit} --- {visited_nodes}")

                if cur_node == -1:  # Empty link
                    continue

                if visited_nodes[cur_node] == 0:  # Not visited
                    print(f"Adding {leftChild[cur_node]} and {rightChild[cur_node]}")
                    tovisit.append(leftChild[cur_node])
                    tovisit.append(rightChild[cur_node])

                visited_nodes[cur_node] += 1

            print(f"For i = {i} , have {visited_nodes}")
            if all(x <= 1 for x in visited_nodes) \
                    and 1 in visited_nodes:
                bin_trees += 1
            for j in range(n):
                visited_nodes[j] = 0 if not visited_nodes[j] else -9999
            print(f"For i = {i} , have purged {visited_nodes}")

        return bin_trees == 1


if __name__ == '__main__':
    sol = Solution()

    # print("Case 1")
    # n = 4
    # leftChild = [1, -1, 3, -1]
    # rightChild = [2, -1, -1, -1]
    # assert sol.validateBinaryTreeNodes(n, leftChild, rightChild)
    #
    # print("Case 2")
    # n = 4
    # leftChild = [1, -1, 3, -1]
    # rightChild = [2, 3, -1, -1]
    # assert not sol.validateBinaryTreeNodes(n, leftChild, rightChild)
    #
    # print("Case 3")
    # n = 2
    # leftChild = [1, 0]
    # rightChild = [-1, -1]
    # assert not sol.validateBinaryTreeNodes(n, leftChild, rightChild)
    #
    # print("Case 4")
    # n = 6
    # leftChild = [1,-1,-1,4,-1,-1]
    # rightChild = [2, -1, -1, 5, -1, -1]
    # assert not sol.validateBinaryTreeNodes(n, leftChild, rightChild)
    #
    # print("Case 5")
    # n = 6
    # lc = [1, -1, -1, 4, -1, -1]
    # rc = [2, -1, -1, 5, -1, -1]
    # assert not sol.validateBinaryTreeNodes(n,lc,rc)

    n= 5
    lc = [0, -1, 3, 1, 3]
    rc = [4, 3, 0, 1, -1]
    assert not sol.validateBinaryTreeNodes(n,lc,rc)