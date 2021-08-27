#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (66.80%)
# Likes:    1222
# Dislikes: 0
# Total Accepted:    185.3K
# Total Submissions: 277.6K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 进阶：
#
#
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
#
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
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
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 
#
# 使用归并排序的时间复杂度是O(n log n)，常数级空间复杂度
# 这里是找到链表的中心位置，切割成两个链表，直到每个都是单个元素
# 然后将这些单个元素（认为他们是有序的）合并起来-->lc.21
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def getMid(head: ListNode, tail: ListNode) -> ListNode:
            slow=fast=head
            while fast!=tail:
                slow=slow.next
                fast=fast.next
                if fast!=tail:
                    fast=fast.next
            return slow
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            preHead=ListNode()
            pre=preHead
            while l1 and l2:
                if l1.val<=l2.val:
                    pre.next=l1
                    l1=l1.next
                else:
                    pre.next=l2
                    l2=l2.next
                pre=pre.next
            pre.next=l1 if l1 is not None else l2
            return preHead.next
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next==tail:
                head.next=None
                return head
            mid=getMid(head,tail)
            return merge(sortFunc(head,mid),sortFunc(mid,tail))
        return sortFunc(head,None)
# @lc code=end
