#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_left, pre_right, in_left, in_right):
            # 跳出
            if pre_left > pre_right or in_left > in_right:
                return None
            # 根节点值
            rootVal = preorder[pre_left]
            root = TreeNode(rootVal)
            # 根节点在中序遍历中的位置，这里使用hash表来保存，加速计算
            pIndex = index[rootVal]
            # 左子树的结点个数
            leftSize = pIndex-in_left
            root.left = helper(pre_left+1, pre_left +
                               leftSize, in_left, pIndex-1)
            root.right = helper(pre_left+leftSize+1,
                                pre_right, pIndex+1, in_right)
            return root
        n = len(preorder)
        index = {val: i for i, val in enumerate(inorder)}
        return helper(0, n-1, 0, n-1)
# @lc code=end
