# 核心代码版本
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
# 
import collections


class Solution:
    def set(self, x, y):
        if x in self.queue:
            # 原先有值，删除后再更新，为了更新在队列中的位置
            self.queue.pop(x)
        else:
            # 不在队列中，需要占用一个缓存
            if self.length > 0:
                self.length -= 1
            else:
                self.queue.popitem(last=False)
        # 插入键值对
        self.queue[x] = y

    def get(self, x):
        # 不在队列
        if x not in self.queue:
            return -1
        # 获取值，并更新位置——先删除，再添加
        val = self.queue.pop(x)
        self.queue[x] = val
        return val
    # 程序入口
    def LRU(self, operators, k):
        # write code here
        # 使用插入有序字典
        self.queue = collections.OrderedDict()
        self.length = k

        res = []
        for op in operators:
            if op[0] == 1:
                self.set(op[1], op[2])
            elif op[0] == 2:
                val = self.get(op[1])
                res.append(val)
        return res
