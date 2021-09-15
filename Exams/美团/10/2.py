# 与n不相邻的最小的数字
# 排成杨辉三角的样式
class Yanghui:
    def calc(self,n):
        if n<4:
            return -1
        elif n==4:
            return 3
        elif n==5:
            return 1
        left=[1]
        for i in range(1,n):
            left.append(left[-1]+i)
        if n in left:
            return n-1
        return n-2


yh=Yanghui()
n=int(input().strip())
res=yh.calc(n)
print(res)
