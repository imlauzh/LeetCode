#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        if n == 1:
            return nums[0] == target
        i, j = 0, n-1
        # 左右边界可以相等
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return True
            # 与33题不同, 元素可以出现多次
            # 所以当左边界与中指相等时,无法判断哪边是有序的
            # 所以两边同时缩减, 下次再判断
            if nums[i] == nums[mid] == nums[j]:
                i += 1
                j -= 1
            elif nums[i] < nums[mid]:
                # [i,mid]
                if nums[i] <= target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                # [mid,r]
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return False
# @lc code=end
