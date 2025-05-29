#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, idx = 0, n-1, n-1
        ans = [0]*n
        while l<=r:
            if pow(nums[l], 2)>pow(nums[r], 2):
                ans[idx] = pow(nums[l], 2)
                l+=1
            else:
                ans[idx] = pow(nums[r], 2)
                r-=1
            idx-=1
        return ans
# @lc code=end

