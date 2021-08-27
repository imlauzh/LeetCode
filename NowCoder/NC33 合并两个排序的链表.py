# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        preHead = ListNode(0)
        curr = preHead
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                curr.next = pHead1
                pHead1 = pHead1.next
            else:
                curr.next = pHead2
                pHead2 = pHead2.next
            curr = curr.next
        curr.next = pHead1 if pHead1 else pHead2
        return preHead.next
