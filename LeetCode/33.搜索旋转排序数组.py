#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                # [l, mid-1]有序
                if nums[0] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                # [mid, r]有序
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
# @lc code=end
