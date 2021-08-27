#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 剑指 Offer 36. 二叉搜索树与双向链表


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            # 记录头节点
            if not self.prev:
                self.head = curr
            else:
                # 更改左右方向
                # prev-><-curr
                self.prev.right, curr.left = curr, self.prev
            # update prev
            self.prev=curr
            dfs(curr.right)

        if not root:
            return
        # prev init None
        self.prev = None
        dfs(root)
        # prev in tail now
        # add connection
        self.head.left, self.prev.right = self.prev, self.head
        return self.head
# @lc code=end
