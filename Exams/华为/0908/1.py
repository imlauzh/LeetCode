"""
问题
给出一颗二叉树，每个节点有一个编号和一个值，该值可能为负数，请你找出一个最优节点(除根节点外)，使得在该节点将树分成两棵树后(原来的树移除这个节点及其子节点，新的树以该节点为根节点)，分成的两棵树各 节点的和之间的差绝对值最大。请输出该节点编号，如有多个相同的差，输出编号最小的节点。

输入
4
4 9 -7 -8
0 1
0 3
1 2
第一行，四个节点，编号0-3，范围为1-10000
第二行，节点0-3的权值
第三行到第五行，表示二叉树各节点间的父子关系
0 1 // 节点0的左节点是1
0 3 // 节点0的右节点是3
1 2 // 节点1的左节点是2
注意:左节点永远出现在右节点之前
0:4
/ \
1:9 3:-8
/
2:-7

输出
节点编号，示例中编号为3的节点是最优节点
"""


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.path = None


class BestNode:
    def calc(self, n, nodes):
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            node.path = left+right+node.val
            return node.path
        dfs(nodes[0])
        index, res = 0, abs(nodes[0].path-2*nodes[1].path)
        nodeSum = nodes[0].path
        for i in range(2, n):
            tmp = abs(nodeSum-2*nodes[i].path)
            if tmp > res:
                index, res = i, tmp
        return index


bn = BestNode()
n = int(input().strip())
nodes = [TreeNode(int(i)) for i in input().strip().split(' ')]
while True:
    try:
        l, r = [int(i) for i in input().strip().split(' ')]
        if not nodes[l].left:
            nodes[l].left = nodes[r]
        else:
            nodes[l].right = nodes[r]
    except EOFError:
        break
res = bn.calc(n, nodes)
print(res)
