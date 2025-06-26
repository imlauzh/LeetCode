#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            l_len = dfs(node.left)+1
            r_len = dfs(node.right)+1
            nonlocal ans
            ans = max(ans, l_len+r_len)
            return max(l_len, r_len)
        dfs(root)
        return ans
# @lc code=end

