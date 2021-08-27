# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.stack_min:
            self.stack_min.append(node)
        elif node < self.stack_min[-1]:
            self.stack_min.append(node)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self):
        # write code here
        self.stack.pop()
        self.stack_min.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        return self.stack_min[-1]
