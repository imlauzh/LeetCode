# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 链表法
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast = pHead
        slow = pHead

        while True:
            if not (fast and fast.next):
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


# hash
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        seen = []
        if not pHead:
            return None
        while pHead:
            if pHead in seen:
                return pHead
            seen.append(pHead)
            pHead = pHead.next
