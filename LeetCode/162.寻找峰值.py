#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
# 递归, 二分
# 认为虽然无序，但是题目指出数组可能包含多个峰值
# 那么数组是由多个升序降序序列组成的
# 当mid比下一个大，说明峰值在mid左边，
# 小的时候，峰值在mid右边，
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(left, right):
            if left == right:
                return left
            mid = left+(right-left)//2
            if nums[mid] > nums[mid+1]:
                return binarySearch(left, mid)
            else:
                return binarySearch(mid+1, right)

        return binarySearch(0, len(nums)-1)


# 迭代，二分
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(left, right):
            while left <= right:
                if left == right:
                    return left
                mid = left+(right-left)//2
                if nums[mid] > nums[mid+1]:
                    right = mid
                else:
                    left = mid+1
            return -1

        return binarySearch(0, len(nums)-1)


# 线性搜索
# 只需要判断是否大于下一个元素即可，分三种情况讨论
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1
# @lc code=end
