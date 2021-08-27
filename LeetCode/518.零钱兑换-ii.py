#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount+1):
                dp[i]+=dp[i-c]
        return dp[amount]
# @lc code=end

