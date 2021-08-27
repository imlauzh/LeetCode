# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        seen = set()
        while pHead1:
            seen.add(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in seen:
                return pHead2
            pHead2 = pHead2.next
        return None
