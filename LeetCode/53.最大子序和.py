#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# 前缀和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 0
        res = nums[0]
        for i in range(n):
            pre = max(pre+nums[i], nums[i])
            res = max(res, pre)
        return res


# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=max(nums[i-1],0)
        return max(nums)


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=max(nums[i-1],0)
        return max(nums)
# @lc code=end
