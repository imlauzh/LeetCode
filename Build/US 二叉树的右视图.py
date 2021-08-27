# encoding: utf-8
from tree import TreeNode, Tree


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


class Solution:
    def sovle(self, root):
        dicta = {}
        stack = []
        index = 0
        maxlen = 0
        stack.append([root, 0])
        while len(stack) > 0:
            n = stack.pop(0)
            node, index = n[0], n[1]
            if node:
                maxlen = max(maxlen, index)
                dicta.setdefault(index, node.val)
                stack.append([node.right, index+1])
                stack.append([node.left, index+1])
        res = []
        for i in range(maxlen+1):
            res.append(dicta[i])
        return res


if __name__ == '__main__':
    s = Solution()
    nodes = [1, 2, 3, '#', '#', 4, 5]
    tree = Tree(TreeNode(nodes[0]))
    tree.buildTree(nodes)
    tree.printTree()
    res = s.sovle(tree.rootNode)
    print(res)
