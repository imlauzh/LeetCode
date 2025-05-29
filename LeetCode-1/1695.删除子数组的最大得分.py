#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = cur_sum = 0
        num_freq = defaultdict(int)
        n = len(nums)
        l, r = 0, 0
        while r < n:
            num_freq[nums[r]] += 1
            cur_sum += nums[r]
            while num_freq[nums[r]] > 1 and l < r:
                num_freq[nums[l]] -= 1
                if num_freq[nums[l]] == 0:
                    del num_freq[nums[l]]
                cur_sum -= nums[l]
                l += 1
            if len(num_freq) == r - l + 1:
                ans = max(ans, cur_sum)
            r += 1
        return ans
# @lc code=end

