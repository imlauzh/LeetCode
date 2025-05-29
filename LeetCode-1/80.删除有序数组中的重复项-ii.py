#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
# 快慢指针，关键在于数字最多可以重复2次

# 输入：nums = [0,0,1,1,1,1,2,3,3]
# 输出：7, nums = [0,0,1,1,2,3,3]

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2: return nums
        l,r = 2,2
        while r<n:
            if nums[r]!=nums[l-2]:
                nums[l] = nums[r]
                l+=1
            r+=1
        return l
# @lc code=end

