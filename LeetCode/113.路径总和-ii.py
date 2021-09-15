#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
# 回溯
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backTrack(root, target):
            if not root:
                return
            # 更新值
            target -= root.val
            path.append(root.val)
            # 递归操作
            if not (root.left or root.right) and target == 0:
                res.append(path[:])
            backTrack(root.left, target)
            backTrack(root.right, target)
            # 还原值
            path.pop()
            target += root.val
        res = []
        path = []
        backTrack(root, targetSum)
        return res


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backTrack(target, root):
            if not root:
                return
            target -= root.val
            path.append(root.val)
            if not (root.left or root.right) and target == 0:
                res.append(path[:])
            backTrack(target, root.left)
            backTrack(target, root.right)
            path.pop()
            target += root.val
        res = []
        path = []
        backTrack(targetSum, root)
        return res
# @lc code=end
