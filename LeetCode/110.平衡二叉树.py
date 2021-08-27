#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            leftH=height(root.left)
            if leftH==-1:
                return -1
            rightH=height(root.right)
            if rightH==-1 or abs(leftH-rightH)>1:
                return -1
            else:
                return max(leftH,rightH)+1
        return height(root)>=0
# @lc code=end

