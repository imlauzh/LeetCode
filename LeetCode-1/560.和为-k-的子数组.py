#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        ans = 0
        cnt = defaultdict(int)
        for j in s:
            ans += cnt[j - k]
            cnt[j] += 1
        return ans

# @lc code=end

