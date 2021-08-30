#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        curr = prev
        while curr:
            value = prev.val
            while curr.next and curr.next.val == value:
                curr = curr.next
            prev.next = curr.next
            prev = curr.next
            curr = prev
        return head
# @lc code=end
