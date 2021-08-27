# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类 the root
# @return bool布尔型一维数组
#
class Solution:
    def judgeIt(self, root):
        # write code here
        def judgeBST(root, minVal, maxVal):
            if not root:
                return True
            if not minVal < root.val < maxVal:
                return False
            return judgeBST(root.left, minVal, root.val) and judgeBST(root.right, root.val, maxVal)

        def judgeComplete(root):
            if not root:
                return True
            import collections
            q = collections.deque()
            q.append(root)
            left = False
            while q:
                node = q.popleft()
                if not node:
                    left = True
                    continue
                else:
                    if left:
                        return False
                    q.append(node.left)
                    q.append(node.right)
            return True
        return [judgeBST(root, float('-inf'), float('inf')), judgeComplete(root)]
