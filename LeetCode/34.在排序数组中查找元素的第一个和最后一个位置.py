#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
class Solution(object):
    def searchRange(self, nums, target):
        # 第一个小于等于target的位置
        def binaryLeft(nums, target):
            n = len(nums)-1
            left = 0
            right = n
            while(left <= right):
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid-1
                if nums[mid] < target:
                    left = mid+1
            return left
        a = binaryLeft(nums, target)
        b = binaryLeft(nums, target+1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b-1]


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


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)-1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        else:
            return [left, right]


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch():
            left, right = 0, n-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        n = len(nums)
        index = binarySearch()
        if index == -1:
            return [-1, -1]
        left = right = index
        while left-1 >= 0 and nums[left-1] == target:
            left -= 1
        while right+1 < n and nums[right+1] == target:
            right += 1
        return [left, right]
# @lc code=end
