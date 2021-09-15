# 搬家具，01背包问题


class Solution:
    def maxLength(self, capacity, values, weight):
        num = values[0]
        values = values[1:]
        weight = weight[1:]
        dp = [[0]*(capacity+1) for _ in range(num+1)]
        for i in range(1, num+1):
            for j in range(1, capacity+1):
                dp[i][j] = dp[i-1][j]
                if j >= weight[i-1] and dp[i][j] < dp[i-1][j-weight[i-1]] + values[i-1]:
                    dp[i][j] = dp[i-1][j-weight[i-1]]+values[i-1]
        return dp[num][capacity]


s = Solution()
capacity = int(input().strip())
values = input().strip()
values = list(map(int, values.split(' ')))
weight = input().strip()
weight = list(map(int, weight.split(' ')))
res = s.maxLength(capacity, values, weight)
print(res)
