#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
# 考虑数组中的最后一个元素 x：在最小值右侧的元素（不包括最后一个元素本身），它们的值一定都严格小于 x；而在最小值左侧的元素，它们的值一定都严格大于 x
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


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,n-1
        while left<right:
            if nums[left]<nums[right]:
                return nums[left]
            mid=(left+right)//2
            if nums[mid]==nums[right]:
                right-=1
            elif nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]
# @lc code=end
