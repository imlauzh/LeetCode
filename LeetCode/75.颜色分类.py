#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# 虽然是一次遍历，但是使用了O(n)的空间复杂度
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        c = 0
        for color in [0, 1, 2]:
            if color in count:
                for i in range(count[color]):
                    nums[c] = color
                    c += 1


# 单指针+遍历两边
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                swap(i, index)
                index += 1
        for i in range(index, len(nums)):
            if nums[i] == 1:
                swap(i, index)
                index += 1


# 双指针，一遍遍历
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        n = len(nums)
        i, idx0, idx2 = 0, 0, n-1
        while i <= idx2:
            # 把当前位置和尾巴的2全都放到尾巴，用while循环
            while i <= idx2 and nums[i] == 2:
                swap(i, idx2)
                idx2 -= 1
            if nums[i] == 0:
                swap(i, idx0)
                idx0 += 1
            i += 1


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        n = len(nums)
        i, idx0, idx2 = 0, 0, n-1
        while i <= idx2:
            # 把当前位置和尾巴的2全都放到尾巴，用while循环
            while i <= idx2 and nums[i] == 2:
                swap(i, idx2)
                idx2 -= 1
            if nums[i] == 0:
                swap(i, idx0)
                idx0 += 1
            i += 1
# @lc code=end
