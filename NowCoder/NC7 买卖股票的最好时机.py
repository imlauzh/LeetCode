#
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices):
        # write code here
        n = len(prices)
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, n):
            maxProfit = max(maxProfit, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return maxProfit
