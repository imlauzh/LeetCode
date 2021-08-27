#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点

# 根据长度删除结点 O(L),O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        hair = ListNode(0, head)
        length = getLength(head)
        curr = hair
        for _ in range(1, length - n + 1):
            curr = curr.next
        curr.next = curr.next.next
        return hair.next


# 栈，O(L),O(L)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        hair = ListNode(0, head)
        stack = list()
        cur = hair
        while cur:
            stack.append(cur)
            cur = cur.next

        for _ in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return hair.next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        hair = ListNode(0, head)
        first = head
        second = hair
        for i in range(n):
            first = first.next
        while first:
            second = second.next
            first = first.next
        second.next = second.next.next
        return hair.next
# @lc code=end
