#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combines = [0]*k
        
        def backTrack(pos, count):
            if count == k:
                res.append(combines[:])
                return
            for i in range(pos, n+1):
                combines[count] = i
                backTrack(i+1, count+1)
        backTrack(1, 0)
        return res
# @lc code=end
