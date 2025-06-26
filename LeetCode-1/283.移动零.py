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
        # double point，快慢指针，慢：不为零，快：正常遍历
        idx = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx +=1
            
# @lc code=end

