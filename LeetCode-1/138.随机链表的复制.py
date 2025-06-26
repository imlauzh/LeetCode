#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        new_head = head.next
        cur = head
        while cur.next.next:
            copy = cur.next
            cur.next = copy.next
            copy.next = copy.next.next
            cur = cur.next
        cur.next = None
        return new_head

# @lc code=end

