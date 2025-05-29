#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
# 动态规划，关键是转移方程

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
# @lc code=end

