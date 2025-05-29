#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
# dp[x] = dp[x-i] + 1

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0
        dp = [10001]*(amount+1)
        for c in coins:
            if c<amount:
                dp[c] = 1
            if c==amount:
                return 1
        for i in range(1, amount+1):
            for j in coins:
                if i-j>=1:
                    dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[amount] if dp[amount]<=10000 else -1
# @lc code=end

