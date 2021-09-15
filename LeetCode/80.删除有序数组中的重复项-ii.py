#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # 长度小于2 的必然可以保留
        if n <= 2:
            return n
        # 从第三个开始计算
        # 前两个可以不用考虑
        fast = slow = 2
        while fast < n:
            # slow是当前需要更改的值
            # 当前fast不等于slow-2时，才更新slow
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end
