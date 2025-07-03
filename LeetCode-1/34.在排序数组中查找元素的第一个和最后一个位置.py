#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)
        while l+1<r:
            mid = (l+r)//2
            if nums[mid]<target:
                l=mid
            else:
                r=mid
        return r
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = self.lower_bound(nums, target)
        if s==len(nums) or nums[s]!=target:
            return [-1, -1]
        e = self.lower_bound(nums, target+1)-1
        return [s, e]
# @lc code=end

