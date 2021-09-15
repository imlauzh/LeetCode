#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# 快慢指针两次相遇
# 双指针第一次相遇： 如果fast指针是空或者next是空，则说明链表没有环
# 否则的话，两个指针一定会相遇，其中fast=2*slow, 链表长度为n=a+b，到链表入口为a，环长度为b，那么相遇时有s=m*b
# 那么fast先放置回head，则下一次相遇的时候，slow=m*b+fast=fast成立，由于链表有环，那么只有当fast=a时才成立，此时就是链表入口的位置

# 环长就是相遇后再次相聚slow走的距离
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=fast=head
        while True:
            if not (fast and fast.next):
                return
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        fast=head
        while fast!=slow:
            slow=slow.next
            fast=fast.next
        return slow


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if not (fast and fast.next):
                return
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow
# @lc code=end
