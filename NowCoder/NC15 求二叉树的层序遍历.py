# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
# 递归
class Solution:
    def __init__(self):
        self.ret = []

    def order(self, root, depth):
        if not root:
            return
        while len(self.ret) < depth+1:
            self.ret.append([])
        self.ret[depth].append(root.val)
        self.order(root.left, depth+1)
        self.order(root.right, depth+1)

    def levelOrder(self, root):
        # write code here
        depth = 0
        self.order(root, depth)
        return self.ret


# 队列
class Solution:
    def levelOrder(self, root):
        # write code here
        queue, ret = [], []
        if not root:
            return ret
        queue.append(root)
        while len(queue):
            n = len(queue)
            tmp = []
            for i in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(tmp)
        return ret
