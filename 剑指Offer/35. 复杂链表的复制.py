"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# 使用哈希表映射旧结点与复制结点
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic = {}
        curr = head
        # 先复制存在的结点
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        # 再处理映射
        while curr:
            dic[curr].next = dic.get(curr.next)
            dic[curr].random = dic.get(curr.random)
            curr = curr.next
        return dic[head]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res      # 返回新链表头节点
