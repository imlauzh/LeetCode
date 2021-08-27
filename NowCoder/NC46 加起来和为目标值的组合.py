#
#
# @param num int整型一维数组
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def combinationSum2(self , num , target ):
        # write code here
        def dfs(path,target,start):
            if target<0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(start,n):
                if (i>start and num[i] == num[i-1]) or target<num[i]:
                    continue
                dfs(path+[num[i]],target-num[i],i+1)
        res = []
        n = len(num)
        num.sort()
        dfs([],target,0)
        return res