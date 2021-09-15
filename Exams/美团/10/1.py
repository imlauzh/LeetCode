# 有多少个长度为n的仅由a，b组成的字符串既不包含aba，bab
# 回溯时间会超，找规律做
class abString:
    def getNum(self, n):
        def backTrack(index):
            nonlocal res
            if index == n:
                res += 1
                return
            if index < 2 or path[index-1] == path[index-2]:
                path[index] = 'a'
                backTrack(index+1)
                path[index] = 'b'
                backTrack(index+1)
            elif index >= 2 and path[index-1] != path[index-2]:
                path[index] = path[index-1]
                backTrack(index+1)
        res = 0
        path = ['a']*n
        backTrack(0)
        return res % 998244353

    def fib(self, n):
        a, b = 2, 2
        for i in range(n):
            a, b = b, a+b
        return a % 998244353


ab = abString()
n = int(input().strip())
res = ab.fib(n)
print(res)
