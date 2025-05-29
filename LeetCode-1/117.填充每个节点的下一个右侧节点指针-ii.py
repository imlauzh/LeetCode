#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
# 首先判断节点的右侧节点是哪一个
# 递归函数：找一个节点的右侧节点：

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = deque([root])
        while queue:
            n = len(queue)
            last = None
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if last:
                    last.next = node
                last = node
        return root
# @lc code=end

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        cur = root
        while cur:
            dummy = pre = Node() # 虚节点作为每一层链表的开始
            while cur:
                if cur.left:
                    pre.next = cur.left # 依次左节点
                    pre = pre.next # 指针进位
                if cur.right:
                    pre.next = cur.right 
                    pre = pre.next 
                cur = cur.next # root无next跳过，其他节点正常循环，因为前面一层循环已经设置了next，依次把下一层的孩子节点串起来
            cur = dummy.next # 此时的dummy为下一层的开始
        return root
# @lc code=end