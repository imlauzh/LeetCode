#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
# 1. 快慢指针，一个走一次，一个走两次，慢指针就是中间节点

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
# @lc code=end

