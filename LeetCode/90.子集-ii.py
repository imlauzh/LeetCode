#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backTrack(pos):
            res.append(subset[:])
            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backTrack(i+1)
                subset.pop()
        nums.sort()
        backTrack(0)
        return res
# @lc code=end
