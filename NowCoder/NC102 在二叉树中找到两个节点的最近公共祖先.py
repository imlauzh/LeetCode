# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root, o1, o2):
        # write code here
        def dfs(root, o1, o2):
            if not root:
                return None
            if root.val == o1 or root.val == o2:
                return root
            left = dfs(root.left, o1, o2)
            right = dfs(root.right, o1, o2)
            if not left and not right:
                return None
            if not left:
                return right
            if not right:
                return left
            return root
        return dfs(root, o1, o2).val
