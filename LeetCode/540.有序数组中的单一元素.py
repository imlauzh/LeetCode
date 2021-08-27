#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(0, n-1, 2):
            print(i)
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]
# @lc code=end
