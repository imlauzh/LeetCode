# -*- coding:utf-8 -*-
# 思想就是: 栈1用来作入队列
# 栈2用来出队列，当栈2为空时，栈1全部出栈到栈2,栈2再出栈（即出队列）
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
