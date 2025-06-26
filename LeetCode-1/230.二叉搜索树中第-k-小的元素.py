#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, ans
            if node is None or k==0:
                return
            dfs(node.left)
            k-=1
            if k==0:
                ans = node.val
            dfs(node.right)
        dfs(root)
        return ans
# @lc code=end

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1  # 题目保证节点值非负，用 -1 表示没有找到
            left_res = dfs(node.left)
            if left_res != -1:  # 答案在左子树中
                return left_res
            nonlocal k
            k -= 1
            if k == 0:  # 答案就是当前节点
                return node.val
            return dfs(node.right)  # 右子树会返回答案或者 -1
        return dfs(root)
    