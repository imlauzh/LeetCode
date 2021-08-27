# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        first,second=head,head
        for _ in range(k):
            first=first.next
        while first:
            first,second=first.next,second.next
        return second