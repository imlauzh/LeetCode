# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, vin):
        # write code here
        def buildTree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None
            rootVal = pre[pre_left]
            root = TreeNode(rootVal)
            pIndex = index[rootVal]
            left_size = pIndex-in_left
            root.left = buildTree(pre_left+1, pre_left +
                                  left_size, in_left, pIndex-1)
            root.right = buildTree(pre_left+left_size+1,
                                   pre_right, pIndex+1, in_right)
            return root
        n = len(pre)
        index = {val: i for i, val in enumerate(vin)}
        return buildTree(0, n-1, 0, n-1)
