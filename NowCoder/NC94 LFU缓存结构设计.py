#
# lfu design
# @param operators int整型二维数组 ops
# @param k int整型 the k
# @return int整型一维数组
#
from collections import OrderedDict

"""
思路：
(1) 要get()时间复杂度O(1),则一定要有一个字典，存储所有的Key-Value
(2) 要删除访问最少的，则必须能快速找到最小是几，无序遍历比较-->有变量(min)保存当前最小是几
(3) 要删除访问最少的，则必须根据访问次数(num)能找到对应的Item有哪些 --> Map存储num到Items(一批元素)的映射
(4) 要删除最早的,则Items必须要有有序结构，可以O(1)找到最早加入的Item,这个结构可以很多，比如数组，链表，因为Item是Key-Value结构,我们这里使用有序字典(OrderedDict)最合适
(5) 插入时要知道自己所在的OrderedDict,所以Value不仅是value,还要有count
"""


class Solution:
    class Node(object):
        def __init__(self, key, value, count):
            self.key = key
            self.value = value
            self.count = count

    class LFUCache(object):
        def __init__(self, maxsize):
            self.db = {}  # DB
            # self.num_order_dict = {}  # 结构DB,存储num到Items(OrderedDict)的映射
            self.num_order_dict = OrderedDict()  # 结构DB,存储num到Items(OrderedDict)的映射
            self.maxsize = maxsize
            self.min = 0

        def pop(self):
            """淘汰策略"""
            # 从结构DB删除
            # 找到频次最小的OrderedDict
            order_dict = self.num_order_dict[self.min]
            # 删除其第一个元素
            _, node = order_dict.popitem(last=False)
            print("删除%s=%s" % (str(node.key), str(node.value)))
            # 从存储DB删除
            del self.db[node.key]

        def increase_access_count(self, node):
            key = node.key
            count = node.count
            # 从旧的OrderedDict删除
            order_dict = self.num_order_dict[count]
            print(list(order_dict.keys()))
            print("key = " + str(key))
            del order_dict[key]

            # TODO 如何更新min
            #      如果这个order_dict被直接删除了，那么下一个min在哪里呢？
            #       所以num_order_dict本身也得是有序的
            if 0 < len(order_dict) < self.min:
                self.min = len(order_dict)
            if len(order_dict) == 0:
                del self.num_order_dict[count]
                keys = list(self.num_order_dict.keys())
                if len(keys) > 0:
                    self.min = keys[0]
                else:
                    self.min = count + 1

            # 加入到新的OrderedDict
            count = count + 1
            # TODO 不要忘了修改 node.count的值
            node.count = count
            if count not in self.num_order_dict.keys():
                self.num_order_dict[count] = OrderedDict()
            order_dict = self.num_order_dict[count]
            order_dict[key] = node

        def set(self, key, value):
            if key in self.db:  # 在DB中，就需要访问次数加1，同时移动自己所在的OrderedDict
                node = self.db[key]
                node.value = value
                self.increase_access_count(node)

            else:  # 不在db中，就要加入num=1维持的OrderedDict
                size = len(self.db)
                if size == self.maxsize:
                    self.pop()
                count = 1
                # 如果num=1对应的OrderedDict不存在，则新建一个
                if count not in self.num_order_dict.keys():
                    self.num_order_dict[count] = OrderedDict()
                order_dict = self.num_order_dict[count]
                # 将新元素加入到此OrderedDict
                node = Solution.Node(key, value, count)
                order_dict[key] = node
                self.min = 1

            self.db[key] = node

        def get(self, key):
            if key in self.db:
                node = self.db[key]
                self.increase_access_count(node)
                return node.value
            return -1

        def show(self):
            for key, node in self.db.items():
                print(key, node.value)

    def LFU(self, operators, k):
        # write code here
        # 操作DB
        result = []
        cache = Solution.LFUCache(maxsize=k)
        for operation in operators:
            p = operation[0]
            key = operation[1]
            if p == 1:  # 存数据
                value = operation[2]
                cache.set(key, value)
            if p == 2:  # 取数据
                result.append(cache.get(key))
        return result
