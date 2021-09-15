#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
# 保存结点遍历
# 平均时间复杂度O(n)
class BSTIterator(object):

    def __init__(self, root):
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0


# 核心思想：二叉搜索树的中序遍历是升序序列
# 该题实际上是实现单调栈
# 首先从根节点开始把左孩子都入栈
# 每次调用next时出栈顶，并加入右子树的所有左孩子
# 平均时间复杂度为O(1), 空间复杂度为O(h)
class BSTIterator(object):
    def __init__(self, root):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def next(self):
        curr=self.stack.pop()
        node=curr.right
        while node:
            self.stack.append(node)
            node=node.left
        return curr.val

    def hasNext(self):
        return len(self.stack)>0


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    def __init__(self, root):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def next(self):
        curr=self.stack.pop()
        node=curr.right
        while node:
            self.stack.append(node)
            node=node.left
        return curr.val

    def hasNext(self):
        return len(self.stack)>0
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
