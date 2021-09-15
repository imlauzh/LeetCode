#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = [0]
        for num in nums:
            P.append(P[-1] + (1 - num))
        
        ans = 0
        for right in range(n):
            left = bisect.bisect_left(P, P[right + 1] - k)
            ans = max(ans, right - left + 1)
        
        return ans
# @lc code=end

