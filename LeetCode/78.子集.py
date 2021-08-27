#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backTrack(pos):
            if pos == len(nums):
                res.append(subset[:])
                return
            backTrack(pos+1)
            subset.append(nums[pos])
            backTrack(pos+1)
            subset.pop()
        backTrack(0)
        return res
# @lc code=end
