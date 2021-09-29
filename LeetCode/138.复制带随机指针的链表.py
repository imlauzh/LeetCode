#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic=dict()
        curr=head
        while curr:
            dic[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            dic[curr].next=dic.get(curr.next)
            dic[curr].random=dic.get(curr.random)
            curr=curr.next
        return dic[head]
# @lc code=end

