#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
# 朴素解法
class Solution:
    def merge2List(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        head = ListNode(0)
        pre = head

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = None
        for l in lists:
            res = self.merge2List(res, l)
        return res


# 分治法，两个两个合并，最后合并到一起
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(l1, l2):
            if not l1 or not l2:
                return l1 if l1 else l2
            head = ListNode(0)
            prev = head
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 if l1 else l2
            return head.next

        def divLists(left, right):
            if left == right:
                return lists[left]
            if left > right:
                return None
            mid = left+(right-left)//2
            return merge2Lists(divLists(left, mid), divLists(mid+1, right))
        res = divLists(0, len(lists)-1)
        return res


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 分治法
class Solution:
    def merge2List(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        head = ListNode(0)
        pre = head

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return head.next

    def divMerge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        # 用递归不用循环
        mid = (l+r)//2
        return self.merge2List(self.divMerge(lists, l, mid), self.divMerge(lists, mid+1, r))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.divMerge(lists, 0, len(lists)-1)
# @lc code=end
