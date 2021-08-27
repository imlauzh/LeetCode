#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (20.98%)
# Likes:    3183
# Dislikes: 646
# Total Accepted:    155.8K
# Total Submissions: 742.8K
# Testcase Example:  '[4,2,3]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
#
#
# Example 1:
#
#
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
# Example 2:
#
#
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
#
# 遍历操作，如果当前值比前一个小，就修改值，再去遍历后面的值
# 为了防止修改后的数值出现递减且不会影响之后的判断
# 这里分两种情况考虑，nums[i] >= nums[i-2]，就把中间值改成他们俩大的那个
# nums[i] < nums[i-2]，把后一个值改成前一个值

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i > 1 and nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                elif i > 1 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
        return cnt <= 1
# @lc code=end
