#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -inf
        _sum = 0
        for i, num in enumerate(nums):
            _sum += num
            if i < k - 1:
                continue
            ans = max(ans, _sum)
            _sum -= nums[i - k + 1]
        return ans / k
# @lc code=end

