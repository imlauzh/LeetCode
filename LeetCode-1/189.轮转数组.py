#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
# 按k的位置两次翻转+整体翻转即可轮转
# 注意边界情况：k>len(nums)

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums):
            l,r = 0, len(nums)-1
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            return nums
        nums = reverse(nums)
        k = k if k<=len(nums) else k%len(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
# @lc code=end


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or k == 0:
            return
        k = k % n  
        nums[:] = nums[-k:] + nums[:-k] # python 中 翻转的内置方法
# @lc code=end