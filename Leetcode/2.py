# Name: Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Method: Build new linked list, keep going as long as one head present (or a carry)
# Time: O(n)
# Space: O(n)
# Difficulty: Medium


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Consider case when not same len
        res_head = ListNode()
        res_now = res_head

        l1_head = l1
        l2_head = l2
        carry = 0
        while l1_head or l2_head or carry:
            sum_now = (
                (l1_head.val if l1_head else 0)
                + (l2_head.val if l2_head else 0)
                + carry
            )
            res_now.next = ListNode(sum_now % 10)

            carry = sum_now // 10
            res_now = res_now.next
            l1_head = l1_head.next if l1_head else None
            l2_head = l2_head.next if l2_head else None

        return res_head.next
