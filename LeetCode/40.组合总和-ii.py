#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
# 与39题类似，需要着重考虑如何去除重复


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTrack(target, combine, idx):
            if target == 0:
                res.append(combine[:])
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    return
                # 相同的位置，如果是相同的元素，就不需要加入了
                # 不然会引起重复
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                combine.append(candidates[i])
                backTrack(target-candidates[i], combine, i+1)
                combine.pop()

        res = []
        combine = []
        candidates.sort()
        backTrack(target, combine, 0)
        return res
# @lc code=end
