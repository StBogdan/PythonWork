# Name: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Method: Trailer node that gets pulled along, check for edge case w/ 1 elem
# Time: O(n)
# Space: O(1)
# Difficulty: Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        trailer = head
        dist = 0
        head_now = head
        while head_now is not None:
            if dist > n:
                trailer = trailer.next
            head_now = head_now.next
            dist += 1

        print(trailer)
        if dist > n:
            trailer.next = trailer.next.next  # We know this exists as n >= 1
        else:
            head = head.next
        return head
