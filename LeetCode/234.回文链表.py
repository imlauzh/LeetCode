#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
# 数组辅助判断
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


# 递归
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return recursively_check()


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def endOfFirst(head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if not head:
            return True
        # 左边尾结点
        firstEnd = endOfFirst(head)
        # 右边头结点
        second = reverse(firstEnd.next)
        left, right = head, second
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def endofFirst(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        endFirst = endofFirst(head)
        startSec = reverse(endFirst.next)
        curr = head
        while startSec:
            if curr.val != startSec.val:
                return False
            curr = curr.next
            startSec = startSec.next
        return True
# @lc code=end
