#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0
        for i in range(n-1):
            for j in range(1, min(nums[i]+1, n-i)):
                dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1]
# @lc code=end
