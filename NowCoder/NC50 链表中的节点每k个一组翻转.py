# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def reverse(self,head,tail):
        prev=tail.next
        curr=head
        while prev!=tail:
            nxt=curr.next
            curr.next,prev,curr=prev,curr,nxt
        return tail,head
    def reverseKGroup(self,head, k):
        hair=ListNode(0)
        hair.next=head
        prev=hair
        
        while head:
            tail=prev
            for _ in range(k):
                tail=tail.next
                if not tail:
                    return hair.next
            nxt=tail.next
            head,tail=self.reverse(head, tail)
            prev.next=head
            tail.next=nxt
            prev=tail
            head=prev.next
        return hair.next