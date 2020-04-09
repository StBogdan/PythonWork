#  Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowboie  = head
        fastboye = head
        while fastboye != None:
            fastboye = fastboye.next
            if fastboye:
                slowboie = slowboie.next
                fastboye = fastboye.next
            else:
                break
        return slowboie.val


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(3)
    head.next= ListNode(4)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(6)


    print(sol.middleNode(head))
