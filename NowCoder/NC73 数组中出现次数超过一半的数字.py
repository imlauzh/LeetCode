# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        n = len(numbers)
        seen = dict()
        target = n//2
        for i in numbers:
            if i in seen:
                seen[i] += 1
                if seen[i] > target:
                    return i
            else:
                seen[i] = 1
        return numbers[0]
