#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (40.34%)
# Likes:    6467
# Dislikes: 0
# Total Accepted:    909K
# Total Submissions: 2.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
# 示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
# 提示：
#
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0
# 题目数据保证列表表示的数字不含前导零
#
#
# 朴素做法
class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:
        head, carry = head1, 0
        # 计算都有的位置
        while head1 and head2:
            sumVal = head1.val+head2.val+carry
            head1.val = sumVal % 10
            carry = sumVal//10
            # 记录tail，便于衔接剩下的链表长度
            tail = head1
            head1, head2 = head1.next, head2.next
        # 链表2是长的
        if head2:
            # tail接上链表2
            tail.next = head2
            while carry > 0 and head2:
                sumVal = head2.val+carry
                head2.val = sumVal % 10
                carry = sumVal//10
                # 更新tail
                tail = head2
                head2 = head2.next
        # 链表1是长的
        elif head1:
            while carry > 0 and head1:
                sumVal = head1.val+carry
                head1.val = sumVal % 10
                carry = sumVal//10
                tail = head1
                head1 = head1.next
        # 如果都计算完了还有进位，则在tail后面加上
        if carry > 0:
            carry = ListNode(carry)
            tail.next = carry
        return head


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        # 商和余数
        carry, val = 0, 0
        # 还需要判断一下最后的进位
        while carry or l1 or l2:
            # 上一轮的商这一轮变成进位
            val = carry
            # 更新l1,l2,val
            if l1:
                l1, val = l1.next, l1.val+val
            if l2:
                l2, val = l2.next, l2.val+val

            carry, val = divmod(val, 10)
            # 下面这一句需要注意复制的顺序,等同于
            # _ = ListNode(val)
            # curr.next= _
            # curr=_ -> curr=curr.next
            curr.next = curr = ListNode(val)
        return head.next
# @lc code=end
