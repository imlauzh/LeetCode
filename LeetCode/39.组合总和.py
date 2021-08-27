#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
# 数字可以被无限制使用，那么对于每个状态来说
# 数组中的每一个数字都可以不使用或者使用
# 每次搜索可以延伸出两个分支，分别是使用和不使用
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target,combine,idx):
            if idx==len(candidates):
                return
            if target==0:
                res.append(combine.copy())
                return
            dfs(target,combine,idx+1)
            if target-candidates[idx]>=0:
                combine.append(candidates[idx])
                dfs(target-candidates[idx],combine,idx)
                combine.pop()
            else:
                return
        res=[]
        combine=[]
        candidates.sort()
        dfs(target,combine,0)
        return res


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target,combine,idx):
            if target==0:
                res.append(combine.copy())
                return
            if idx==len(candidates):
                return
            dfs(target,combine,idx+1)
            if target-candidates[idx]>=0:
                combine.append(candidates[idx])
                dfs(target-candidates[idx],combine,idx)
                combine.pop()
            else:
                return
        res=[]
        combine=[]
        candidates.sort()
        dfs(target,combine,0)
        return res
# @lc code=end

