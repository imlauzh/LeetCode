# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        prev = hair
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return hair.next
            else:
                prev = curr
                curr = curr.next
        return hair.next
