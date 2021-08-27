#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left+right)//2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
# @lc code=end

