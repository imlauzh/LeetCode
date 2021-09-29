# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            recur(root.left)
            recur(root.right)
        recur(root)
        return root


# 迭代，辅助栈
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
