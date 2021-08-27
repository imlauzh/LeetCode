# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @param sum int整型
# @return int整型二维数组
#
class Solution:
    def pathSum(self, root, sums):
        # write code here
        res = []
        if not root:
            return res

        def dfs(root, target, path):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                res.append(path[:])
            else:
                dfs(root.left, target, path)
                dfs(root.right, target, path)
            path.pop()
            target += root.val
        dfs(root, sums, [])
        return res
