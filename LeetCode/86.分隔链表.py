#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
# 简单两个dummy结点保存两个分区
# 不需要来回插入，删除结点

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small, large = ListNode(0), ListNode(0)
        smallHead, largeHead = small, large
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        large.next = None
        small.next = largeHead.next
        return smallHead.next
# @lc code=end
