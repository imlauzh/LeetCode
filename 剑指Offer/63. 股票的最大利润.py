class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):
            maxprofit = max(prices[i] - minprice, maxprofit)
            minprice = min(prices[i], minprice)
        return maxprofit
