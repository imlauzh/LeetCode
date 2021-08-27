# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a
