# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0
        a, b = 0, 1
        for i in range(number):
            a, b = b, a+b
        return b


while True:
    try:
        import sys
        s = Solution()
        lines = str(sys.stdin.readline().strip())
        number = int(lines)
        res = s.jumpFloor(number)
        print(f'{res}')
    except:
        break
