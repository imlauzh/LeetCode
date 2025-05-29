#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cur_len = not_one = 0
        l, r = 0, 0
        n = len(nums)
        while r < n:
            cur_len += 1
            if nums[r] != 1:
                not_one += 1
            while not_one > 1 and l <= r:
                if nums[l] != 1:
                    not_one -= 1
                l += 1
                cur_len -= 1
            ans = max(ans, cur_len)
            r += 1
        return ans - 1
# @lc code=end

