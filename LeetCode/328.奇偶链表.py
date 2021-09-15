#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
# 官方题解
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


# 两个指针，分别串起来，最后合并
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd, even = ListNode(0), ListNode(0)
        oddHead, evenHead = odd, even
        flag = True
        while head:
            if flag:
                odd.next = head
                head = head.next
                odd = odd.next
            else:
                even.next = head
                head = head.next
                even = even.next
            flag = not flag
        even.next = None
        odd.next = evenHead.next
        return oddHead.next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
# @lc code=end
