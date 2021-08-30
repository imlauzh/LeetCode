#
# @lc app=leetcode.cn id=1283 lang=python3
#
# [1283] 使结果不超过阈值的最小除数
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calDiv(d):
            return sum((i-1)//d+1 for i in nums) <= threshold
        low, high = 1, max(nums)+1
        while low < high:
            mid = low+(high-low)//2
            if not calDiv(mid):
                low = mid+1
            else:
                high = mid
        return low
# @lc code=end
