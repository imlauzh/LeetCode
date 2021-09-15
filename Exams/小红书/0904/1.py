# 和最大的矩形区域
class NewMate:
    def getMax(self, n, scores):
        tmp = []
        for i in range(n):
            tmp.append(scores[i*n:(i+1)*n])
        scores = tmp
        dp = [0]*n
        res = float('-inf')
        for i in range(n):
            for j in range(n):
                dp[j] = 0
            for j in range(i, n):
                curr = 0
                for k in range(n):
                    dp[k] += scores[j][k]
                    if curr <= 0:
                        curr = dp[k]
                    else:
                        curr += dp[k]
                    if curr > res:
                        res = curr
        return res


mate = NewMate()
n = int(input().strip())
scores = input().strip()
scores = list(map(int, scores.split(' ')))
res = mate.getMax(n, scores)
print(res)
