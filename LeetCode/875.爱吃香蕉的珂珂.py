#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
# 用二分遍历可能的值，去找恰好可以吃完香蕉的k
# 下限是1，上限是香蕉中的最大值，太大了就浪费了
# 计算每堆香蕉需要几个小时可以吃完，求和小于h即满足


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum((p-1)//k+1 for p in piles) <= h
        low = 1
        high = max(piles)
        while low < high:
            mid = low+(high-low)//2
            if not possible(mid):
                low = mid+1
            else:
                high = mid
        return low
# @lc code=end
