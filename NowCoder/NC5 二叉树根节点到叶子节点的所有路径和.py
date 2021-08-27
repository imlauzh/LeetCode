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
    def sumNumbers(self, root):
        # write code here
        # 先序遍历
        if root is None:
            return 0

        def cal(root, sums):
            if root is None:
                return 0
            sums = 10 * sums + root.val
            if root.left is None and root.right is None:
                return sums
            return cal(root.left, sums) + cal(root.right, sums)

        return cal(root, 0)


class Solution:
    def sumNumbers(self, root):
        # write code here
        def dfs(root, num):
            num += str(root.val)
            if not (root.left or root.right):
                self.res += int(num)
            if root.left:
                dfs(root.left, num)
            if root.right:
                dfs(root.right, num)
        if not root:
            return 0
        self.res = 0
        dfs(root, '')
        return self.res
