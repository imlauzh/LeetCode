#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        hair = ListNode(-1)
        hair.next = head
        pre = hair
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            # 纸上画一遍
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return hair.next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        hair = ListNode(-1)
        hair.next = head
        pre = hair
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            # 纸上画一遍
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return hair.next
# @lc code=end
