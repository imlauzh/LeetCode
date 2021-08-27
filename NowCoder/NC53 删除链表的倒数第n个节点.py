# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here
        m = 0
        node = head
        while node:
            m += 1
            node = node.next
        if m == n:
            return head.next
        prev = head
        for _ in range(m-n-1):
            prev = prev.next
        prev.next = prev.next.next if prev.next else None
        return head


class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here
        node = head
        for _ in range(n):
            node = node.next
        if not node:
            return head.next
        prev = head
        while node.next:
            prev = prev.next
            node = node.next
        prev.next = prev.next.next
        return head
