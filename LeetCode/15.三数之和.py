#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# 排序+双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)):
            # 排过序的数组,当前值比0大就肯定不会有满足条件的
            if nums[i] > 0:
                continue
            # 当前值等于前一个值
            # 计算的结果肯定已经被包含了, 跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left]+nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # 重复数字,去除重复
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # 上面L，R没有相等的，也需要更新位置
                    left += 1
                    right -= 1
                elif nums[left]+nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
# @lc code=end
