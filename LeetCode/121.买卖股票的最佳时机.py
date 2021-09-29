#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return maxProfit
# @lc code=end
