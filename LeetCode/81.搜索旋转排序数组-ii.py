#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return nums[0] == target
        left, right = 0, n-1
        # 左右边界可以相等
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return True
            # 与33题不同, 元素可以出现多次
            # 所以当左边界与中指相等时,无法判断哪边是有序的
            # 所以两边同时缩减, 下次再判断
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return False
# @lc code=end
