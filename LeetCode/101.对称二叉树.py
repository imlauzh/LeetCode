#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            return leftNode.val == rightNode.val and check(leftNode.left, rightNode.right) and check(leftNode.right, rightNode.left)
        return check(root.left, root.right)

        
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            return leftNode.val == rightNode.val and check(leftNode.left, rightNode.right) and check(leftNode.right, rightNode.left)
        return check(root.left, root.right)
# @lc code=end
