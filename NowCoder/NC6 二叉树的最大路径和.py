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
    def maxPathSum(self, root):
        # write code here
        def maxGain(root):
            if not root:
                return 0
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)
            path = root.val+leftGain+rightGain
            self.res = max(self.res, path)
            return root.val+max(leftGain, rightGain)
        self.res = float('-inf')
        maxGain(root)
        return self.res
