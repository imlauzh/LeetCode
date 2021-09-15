# 不重叠区间
# 3
# 1,3
# 5,7
# 2,6


class Solution:
    def maxLength(self, inputs):
        inputs.sort(key=lambda x: (x[0], x[1]))
        for i in range(len(inputs)-1):
            if inputs[i][1] > inputs[i+1][0]:
                inputs[i][1], inputs[i+1][0] = inputs[i+1][0], inputs[i][1]
        res = 0
        for i in inputs:
            res += i[1]-i[0]
        return res

    def maxLength1(self, inputs):
        inputs.sort(key=lambda x: x[0])
        res = []
        for i in inputs:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = min(res[-1][1], i[0])
                if res[-1][1] < i[1]:
                    res.append([res[-1][1], i[1]])
                else:
                    res.append([i[1], res[-1][1]])
        ans = 0
        for i in res:
            ans += i[1]-i[0]
        return ans


s = Solution()
n = int(input().strip())
inputs = []
for i in range(n):
    line = input().strip()
    line = list(map(int, line.split(',')))
    inputs.append(line)
res = s.maxLength1(inputs)
print(res)
