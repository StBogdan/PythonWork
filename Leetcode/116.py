from collections import deque

# Method: Modified BF
# Time:  O(n) with n nodes
# Space: O(log(depth))

# Definition for a Node.


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        level_now = deque([root])
        next_level = deque()
        while level_now:
            node_now = level_now.popleft()
            if node_now.left:
                next_level.append(node_now.left)
                next_level.append(node_now.right)
            node_now.next = level_now[0] if level_now else None

            if not level_now:
                level_now = next_level
                next_level = deque()

        return root

    def brige_builder_rec(node: "Node") -> "Node":

        if not node.left:  # We're at a leaf
            return None

        left_side = node.left
        right_side = node.right

        while left_side and right_side:
            left_side.next = right_side
            left_side = left_side.right
            right_side = right_side.left

        brige_builder_rec(node.left)
        brige_builder_rec(node.right)

    def brige_builder_next(root: "Node") -> "Node":
        if not root:
            return None

        node_now = root
        next_node = root.left

        while node_now.left:
            node_now.left.next = cur.right

            if node_now.next:  # Can do rightwards
                node_now.right.next = node_now.next.left
                node_now = node_now.next
            else:
                node_now = next_node
                next_node = node_now.left
