# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        n = len(num)
        if size > n or size <= 0:
            return []
        i = 0
        res = []
        queue = []  # 存储值递减的下标
        while i < n:
            # 队列中最大的值的index大于窗口的最左边的index，过期删去
            if len(queue) > 0 and i-size+1 > queue[0]:
                queue.pop(0)
            # 队列中最小值的小于当前num的值，删去最小值，更新为当前值，保证queue中
            # 存较大的值
            while len(queue) > 0 and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            # 记录窗口中的最大值
            if i >= size-1:
                res.append(num[queue[0]])
            i += 1
        return res
