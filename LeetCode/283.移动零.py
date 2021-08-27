#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, 0
        for i in range(n):
            if nums[i] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
# @lc code=end
