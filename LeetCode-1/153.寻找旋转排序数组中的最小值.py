#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums)-1
        while l+1<r:
            mid = (l+r)//2
            if nums[mid]<nums[-1]:
                r = mid
            else:
                l = mid
        return nums[r]
# @lc code=end

