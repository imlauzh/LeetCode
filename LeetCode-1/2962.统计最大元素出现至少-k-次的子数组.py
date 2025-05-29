#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num, cnt = max(nums), 0
        l, r, ans = 0, 0, 0
        while r<n:
            if nums[r]==max_num:
                cnt+=1
            while cnt>=k:
                if nums[l]==max_num:
                    cnt-=1
                l+=1
            ans+=l
            r+=1
        return ans
# @lc code=end

