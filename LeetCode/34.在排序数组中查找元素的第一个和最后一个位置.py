#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target):
            n-len(nums)
            l, r = 0, n-1
            # 判断条件有两个相等，因为会存在只有一个数字的情况
            while l <= r:
                mid = (l+r)//2
                # 找到相等的数字，直接返回
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        n = len(nums)
        if n == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        mid = binarySearch(nums, target)
        # 没找到该值
        if mid < 0:
            return [-1, -1]
        # 向两边扩展
        lower, upper = mid, mid
        while lower-1 >= 0 and nums[lower-1] == target:
            lower -= 1
        while upper+1 < n and nums[upper+1] == target:
            upper += 1
        return [lower, upper]
# @lc code=end
