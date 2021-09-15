#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumAll = sum(nums)
        if sumAll < target:
            return 0
        elif sumAll == target:
            return len(nums)
        curr, left = 0, 0
        res = float('inf')
        for right in range(len(nums)):
            curr += nums[right]
            if curr >= target:
                while True:
                    if curr-nums[left] < target:
                        break
                    curr -= nums[left]
                    left += 1
                res = min(res, right-left+1)
                curr -= nums[left]
                left += 1
        return res
# @lc code=end
