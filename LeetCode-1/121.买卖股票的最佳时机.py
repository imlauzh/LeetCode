#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
# 暴力：遍历n*(n-1)次, 会超时
# 一次遍历：如果我是在历史最低点买进的，那么我今天卖出能赚多少钱？

# 输入：[7,1,5,3,6,4]
# 输出：5

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2:
            return 0
        l = 0
        res = 0
        while l < n-1:
            r = l+1
            while r<n:
                if r<n and prices[r]>prices[l]:
                    res = max(res, prices[r] - prices[l])
                r+=1
            l+=1
        return res
# @lc code=end


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2:
            return 0
        minprice, maxprofit = 100000, 0
        for p in prices:
            if p<minprice:
                minprice = p
            elif maxprofit<p-minprice:
                maxprofit = p-minprice
        return maxprofit
# @lc code=end
