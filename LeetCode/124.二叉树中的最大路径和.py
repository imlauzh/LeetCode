#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            # 当前结点的最大路径和为，结点值+左边最大增益值+右边最大增益
            # 具体意义为，路径的两端在左右子树中，经过父节点
            nodePath = node.val+leftGain+rightGain
            self.maxSum = max(self.maxSum, nodePath)
            # 返回值只有一条边
            return node.val+max(leftGain, rightGain)
        maxGain(root)
        return self.maxSum
# @lc code=end
