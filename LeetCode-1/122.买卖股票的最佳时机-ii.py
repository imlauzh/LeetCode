#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
# 统计所有的上升区间

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        cur = 1
        while cur<len(prices):
            if prices[cur]>prices[cur-1]:
                maxprofit+=prices[cur]-prices[cur-1]
            cur+=1
        return maxprofit
# @lc code=end

