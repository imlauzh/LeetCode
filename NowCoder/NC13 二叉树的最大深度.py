# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型
#
class Solution:
    def maxDepth(self, root):
        # write code here
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)+1
        rightDepth = self.maxDepth(root.right)+1
        return max(leftDepth, rightDepth)
