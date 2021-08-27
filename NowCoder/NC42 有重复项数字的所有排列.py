#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def permuteUnique(self, num):
        # write code here
        def dfs(idx):
            if idx == n:
                if num not in res:
                    res.append(num[:])
            for i in range(idx, n):
                num[i], num[idx] = num[idx], num[i]
                dfs(idx+1)
                num[i], num[idx] = num[idx], num[i]
        n = len(num)
        res = []
        dfs(0)
        return res
