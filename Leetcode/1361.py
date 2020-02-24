from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = {}

        for i in range(n):
            left, right = leftChild[i], rightChild[i]

            if i == left or i == right:
                return False  # Self loop

            if i in parents and (parents[i] == left or parents[i] == right):  # parent loop
                return False

            if left in parents or right in parents:
                return False

            if left != -1:
                parents[left] = i
            if right != -1:
                parents[right] = i

        # Only one left parentless
        print(f"Parents is {parents}")
        return len(parents) == n - 1


if __name__ == '__main__':
    sol = Solution()

    print("Case 1")
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [2, -1, -1, -1]
    assert sol.validateBinaryTreeNodes(n, leftChild, rightChild)

    print("Case 2")
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [2, 3, -1, -1]
    assert not sol.validateBinaryTreeNodes(n, leftChild, rightChild)

    print("Case 3")
    n = 2
    leftChild = [1, 0]
    rightChild = [-1, -1]
    assert not sol.validateBinaryTreeNodes(n, leftChild, rightChild)

    print("Case 4")
    n = 6
    leftChild = [1, -1, -1, 4, -1, -1]
    rightChild = [2, -1, -1, 5, -1, -1]
    assert not sol.validateBinaryTreeNodes(n, leftChild, rightChild)

    print("Case 5")
    n = 6
    lc = [1, -1, -1, 4, -1, -1]
    rc = [2, -1, -1, 5, -1, -1]
    assert not sol.validateBinaryTreeNodes(n, lc, rc)

    print("Case 6")
    n = 5
    lc = [0, -1, 3, 1, 3]
    rc = [4, 3, 0, 1, -1]
    assert not sol.validateBinaryTreeNodes(n, lc, rc)

    print("Case 7")
    n = 5
    lc = [1, -1, -1, -1, -1]
    rc = [2, -1, -1, 0, 3]
    assert sol.validateBinaryTreeNodes(n, lc, rc)
