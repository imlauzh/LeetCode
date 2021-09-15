#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
class SegmentTree:
    def __init__(self, data, merge):
        '''
        data:传入的数组
        merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''

        self.data = data
        self.n = len(data)
        #  申请4倍data长度的空间来存线段树节点
        self.tree = [None] * (4 * self.n)  # 索引i的左孩子索引为2i+1，右孩子为2i+2
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n-1)

    def query(self, queryLeft, queryRight):
        '''
        返回区间[queryLeft,..,queryRight]的值
        '''
        return self._query(0, 0, self.n-1, queryLeft, queryRight)

    def update(self, index, value):
        # 将data数组index位置的值更新为value,然后递归更新线段树中被影响的各节点的值
        self.data[index] = value
        self._update(0, 0, self.n-1, index)

    def _build(self, treeIndex, left, right):
        '''
        递归创建线段树
        treeIndex : 线段树节点在数组中位置
        left, right : 该节点表示的区间的左,右边界
        '''
        if left == right:
            self.tree[treeIndex] = self.data[left]
            return
        # 区间中点,对应左孩子区间结束,右孩子区间开头
        mid = (left+right) // 2
        # treeIndex的左右子树索引
        leftChild, rightChild = 2 * treeIndex + 1, 2 * treeIndex + 2
        self._build(leftChild, left, mid)
        self._build(rightChild, mid+1, right)
        self.tree[treeIndex] = self._merge(
            self.tree[leftChild], self.tree[rightChild])

    def _query(self, treeIndex, left, right, queryLeft, queryRight):
        '''
        递归查询区间[queryLeft,..,queryRight]的值
        treeIndex : 某个根节点的索引
        left, right : 该节点表示的区间的左右边界
        queryLeft, queryRight: 待查询区间的左右边界
        '''
        if left == queryLeft and right == queryRight:
            return self.tree[treeIndex]

        mid = (left+right) // 2  # 区间中点,对应左孩子区间结束,右孩子区间开头
        leftChild, rightChild = treeIndex * 2 + 1, treeIndex * 2 + 2
        if queryRight <= mid:
            # 查询区间全在左子树
            return self._query(leftChild, left, mid, queryLeft, queryRight)
        elif queryLeft > mid:
            # 查询区间全在右子树
            return self._query(rightChild, mid+1, right, queryLeft, queryRight)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(leftChild, left, mid, queryLeft, mid),
                           self._query(rightChild, mid+1, right, mid+1, queryRight))

    def _update(self, treeIndex, left, right, index):
        '''
        treeIndex:某个根节点索引
        left, right : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if left == right == index:
            self.tree[treeIndex] = self.data[index]
            return
        mid = (left+right)//2
        leftChild, rightChild = 2 * treeIndex + 1, 2 * treeIndex + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(rightChild, mid+1, right, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(leftChild, left, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[treeIndex] = self._merge(
            self.tree[leftChild], self.tree[rightChild])


class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(i, j)


# @lc code=start
class SegmentTree:
    def __init__(self, data, merge):
        self.data = data
        self.n = len(data)
        self._merge = merge
        self.tree = [None]*(4*self.n)
        if self.n:
            self._build(0, 0, self.n-1)

    def _build(self, treeIndex, left, right):
        if left == right:
            self.tree[treeIndex] = self.data[left]
            return
        mid = left+(right-left)//2
        leftChild, rightChild = 2*treeIndex+1, 2*treeIndex+2
        self._build(leftChild, left, mid)
        self._build(rightChild, mid+1, right)
        self.tree[treeIndex] = self._merge(
            self.tree[leftChild], self.tree[rightChild])

    def _query(self, treeIndex, left, right, qleft, qright):
        if left == qleft and right == qright:
            return self.tree[treeIndex]
        mid = left+(right-left)//2
        leftChild, rightChild = 2*treeIndex+1, 2*treeIndex+2
        if qright <= mid:
            return self._query(leftChild, left, mid, qleft, qright)
        elif qleft > mid:
            return self._query(rightChild, mid+1, right, qleft, qright)
        return self._merge(self._query(leftChild, left, mid, qleft, mid), self._query(rightChild, mid+1, right, mid+1, qright))

    def query(self, qleft, qright):
        return self._query(0, 0, self.n-1, qleft, qright)

    def _update(self, treeIndex, left, right, index):
        if left == right == index:
            self.tree[treeIndex] = self.data[index]
            return
        mid = left+(right-left)//2
        leftChild, rightChild = 2*treeIndex+1, 2*treeIndex+2
        if index <= mid:
            self._update(leftChild, left, mid, index)
        else:
            self._update(rightChild, mid+1, right, index)
        self.tree[treeIndex] = self._merge(
            self.tree[leftChild], self.tree[rightChild])

    def update(self, index, value):
        self.data[index] = value
        self._update(0, 0, self.n-1, index)


class NumArray:

    def __init__(self, nums: List[int]):
        self.segmentTree = SegmentTree(nums, lambda x, y: x+y)

    def update(self, index: int, val: int) -> None:
        self.segmentTree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end
