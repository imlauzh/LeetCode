"""
4
0 1 1 0
"""

class HeightSort:
    def calc(self, n, heights):
        res = [-1]*n
        tmp = []
        for i in range(n):
            tmp.insert(heights[i], i)
        for i in range(n):
            res[tmp[i]] = i+1
        return res


hs = HeightSort()
n = int(input().strip())
heights = list(map(int, input().strip().split(' ')))
res = hs.calc(n, heights)
print(' '.join(str(i) for i in res))
