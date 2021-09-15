#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
# hash set
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next
        return None

# 双指针优化空间复杂度


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
# @lc code=end
