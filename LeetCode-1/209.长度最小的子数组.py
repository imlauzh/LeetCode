#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
# 滑动窗口


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n+1
        s, e = 0, 0
        total = 0
        while e<n:
            total+=nums[e]
            while total>=target:
                ans = min(ans, e-s+1)
                total-=nums[s]
                s+=1
            e+=1
        return 0 if ans==n+1 else ans
# @lc code=end

