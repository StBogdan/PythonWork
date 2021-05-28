from collections import Counter
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nr = ""
        while head:
            nr += str(head.val)
            head = head.next
        return int(nr, 2)


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(0)
    print(sol.getDecimalValue(head))
