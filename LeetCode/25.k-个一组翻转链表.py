#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        # 为了衔接下一部分
        # 正常的翻转为None，也就是tail的next
        prev = tail.next
        curr = head
        while prev != tail:
            nxt = curr.next
            curr.next, prev, curr = prev, curr, nxt
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 头的前一个结点是头发
        hair = ListNode(0)
        hair.next = head
        # 初始化prev
        prev=hair

        while head:
            # 初始化tail，从prev开始，算上head正好k个
            tail=prev
            for _ in range(k):
                # 找到k长度的链表
                tail=tail.next
                # 查看剩余部分长度是否大于等于 k
                if not tail:
                    # 前一部分已经连上了，可以直接返回
                    return hair.next
            # 保存下一段的开始
            nxt=tail.next
            head,tail=self.reverse(head,tail)
            # 把子链表重新接回原链表
            prev.next = head
            tail.next = nxt
            prev = tail
            head = tail.next

        return hair.next
# @lc code=end
