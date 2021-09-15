# 奇偶重排，偶数在前，奇数在后
# 8
# 2,1,3,6,4,7,8,5


class Solution:
    def maxLength(self, inputs):
        r1, r2 = [], []
        for i in inputs:
            if i % 2 == 0:
                r1.append(i)
            else:
                r2.append(i)
        return r1+r2


s = Solution()
n = int(input().strip())
inputs = input().strip()
inputs = list(map(int, inputs.split(',')))
res = s.maxLength(inputs)
print(','.join(str(i) for i in res))
