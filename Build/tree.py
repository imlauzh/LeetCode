# encoding: utf-8
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: TreeNode) -> None:
        self.rootNode = root

    def buildTree(self, nodes):
        queue = []
        queue.append(self.rootNode)
        i = 0
        while i < len(nodes):
            parent = queue.pop(0)
            i += 1
            if i < len(nodes):
                if nodes[i] != '#':
                    parent.left = TreeNode(nodes[i])
                    queue.append(parent.left)
            i += 1
            if i < len(nodes):
                if nodes[i] != '#':
                    parent.right = TreeNode(nodes[i])
                    queue.append(parent.right)

    def printTree(self):
        if not self.rootNode:
            print('empty tree')
        queue = []
        res = []
        queue.append(self.rootNode)
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                node = queue.pop(0)
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    tmp.append('#')
            if all(i == '#' for i in tmp):
                continue
            res.append(tmp)
        print(res)
        return res
