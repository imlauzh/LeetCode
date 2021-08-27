#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (71.79%)
# Likes:    1845
# Dislikes: 0
# Total Accepted:    609.6K
# Total Submissions: 847.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
#
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：[2,1]
#
#
# 示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围是 [0, 5000]
# -5000
#
#
#
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
#
#
#

# 迭代
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre=None
#         curr=head
#         while curr:
#             next=curr.next
#             curr.next=pre
#             pre=curr
#             curr=next
#         return pre

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        curr=head
        while curr:
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        return pre
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not (head and head.next):
#             return head
#         new=self.reverseList(head.next)
#         head.next.next=head
#         head.next=None
#         return new
# @lc code=end
