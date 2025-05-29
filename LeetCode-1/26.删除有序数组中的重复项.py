#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
# 非严格递增=》有重复项
# 快慢指针，慢指针代表有效数字，快指针代表下一个有效指针的位置
# 注意最后返回的是数组的长度，即慢指针+1

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            if nums[r]==nums[l]:
                r+=1
            else:
                nums[l+1] = nums[r]
                l+=1
                r+=1
        return l+1
# @lc code=end

