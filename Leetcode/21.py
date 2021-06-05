# Name: Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Method: Zipper merge, with lefover head check
# Time: O(n)
# Space: O(1)
# Difficulty: Easy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_list_head = ListNode()
        head_now = merged_list_head
        l1_head = l1
        l2_head = l2
        while l1_head is not None and l2_head is not None:
            if l1_head.val < l2_head.val:
                head_now.next = l1_head
                l1_head = l1_head.next
            else:
                head_now.next = l2_head
                l2_head = l2_head.next

            head_now = head_now.next
            head_now.next = None

        for leftover_head in (l1_head, l2_head):
            while leftover_head is not None:
                head_now.next = leftover_head
                head_now = head_now.next
                leftover_head = leftover_head.next
        merged_list_head = merged_list_head.next  # Remove dummy start node
        return merged_list_head
