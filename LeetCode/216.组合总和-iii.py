#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        combine=[0]*k
        def backTrack(pos,count,target):
            if count==k and target==0:
                res.append(combine[:])
                return
            if pos>9 or count==k:
                return
            for i in range(pos,10):
                combine[count]=i
                backTrack(i+1,count+1,target-i)

        backTrack(1,0,n)
        return res
# @lc code=end

