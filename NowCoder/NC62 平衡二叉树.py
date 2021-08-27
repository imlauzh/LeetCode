# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, root):
        # write code here
        def getDepth(root):
            if not root:
                return 0
            leftD = getDepth(root.left)
            if leftD == -1:
                return -1
            rightD = getDepth(root.right)
            if rightD == -1 or abs(rightD-leftD) > 1:
                return -1
            else:
                return max(leftD, rightD)+1
        return getDepth(root) >= 0
