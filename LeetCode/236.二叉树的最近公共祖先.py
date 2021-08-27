#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return  # 1.
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        return root  # 2. if left and right:

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # root 的左 / 右子树中都不包含 p,q
        if not left and not right:
            return  # 1.
        # p,q 都不在 rootroot 的左子树中，直接返回 right
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        # p, q 分列在 root的 异侧 （分别在 左 / 右子树）
        # 因此 root 为最近公共祖先，返回 root
        return root  # 2. if left and right:
# @lc code=end
