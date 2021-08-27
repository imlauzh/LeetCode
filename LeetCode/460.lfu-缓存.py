#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#

# @lc code=start
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.freq = 1
        self.next = None
        self.pre = None


class Dlink:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def _append(self, node):
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        self.size += 1

    def _pop_node(self, node=None):
        if not node:
            node = self.head.next
            self.head.next = node.next
            node.next.pre = self.head
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}   # {key:node, ...}
        self.freq = {}       # {key:dlink, ...}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.key_node:
            node = self.key_node[key]
            self.increase_freq_key(key)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        elif key in self.key_node:
            self.key_node[key].val = value
            self.increase_freq_key(key)
        else:
            if len(self.key_node) >= self.capacity:
                self.remove_minfreq_key()
            if 1 not in self.freq:
                self.freq[1] = Dlink()
            node = Node(key, value)
            self.key_node[key] = node
            self.freq[1]._append(node)
            self.min_freq = 1

    def increase_freq_key(self, key):
        """key,freq已经存在"""
        node = self.key_node[key]
        node_freq = node.freq
        self.freq[node_freq]._pop_node(node)
        if self.min_freq == node_freq and self.freq[node_freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq:
            self.freq[node.freq] = Dlink()
        self.freq[node.freq]._append(node)
        self.key_node[key] = node

    def remove_minfreq_key(self):
        node = self.freq[self.min_freq]._pop_node()
        del self.key_node[node.key]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
