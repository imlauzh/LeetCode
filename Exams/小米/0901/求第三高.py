class Solution:
    def calHeight(self, x, y):
        if x == y:
            return 'No Answer'
        left = max(1, floor(x*y/(x+y)))
        right = cell(x*y/(x-y))
        res = []
        if left >= right:
            return 'No Answer'
        for i in range(right-1, left-1, -1):
            res.append(i)
        return ' '.join(res)


s = Solution()
ins = input().strip()
ins = list(map(int, ins.split(' ')))
res = s.calHeight(ins[0], ins[1])
print(res)
