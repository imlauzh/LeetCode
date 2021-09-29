# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        reverse = False
        while queue:
            tmp = []
            n = len(queue)
            for _ in range(n):
                top = queue.pop(0)
                tmp.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            if reverse:
                tmp.reverse()
            res.append(tmp)
            reverse = not reverse
        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        reverse = False
        while queue:
            tmp = []
            n = len(queue)
            for _ in range(n):
                top = queue.pop(0)
                # 更改tmp插入位置
                if not reverse:
                    tmp.append(top.val)
                if reverse:
                    tmp.insert(0,top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(tmp)
            reverse = not reverse
        return res