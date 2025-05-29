#
# @lc app=leetcode.cn id=2875 lang=python3
#
# [2875] 无限数组的最短子数组
#

# @lc code=start
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        ans = inf
        s = 0
        n = len(nums)
        total = sum(nums)
        rem = target % total
        l, r = 0, 0
        while r < n * 2:
            s += nums[r % n]
            while s > rem:
                s -= nums[l % n]
                l += 1
            if s == rem:
                ans = min(ans, r - l + 1)
            r += 1
        return (target // total) * n + ans if ans < inf else -1
# @lc code=end

