#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
# 固定一个数，双指针寻找
# 注意点：三元组去重；剪枝

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n < 3:
            return ans

        nums.sort() # 1. 排序

        for i in range(n - 2): # 2. 主循环，固定第一个数 nums[i]
            # 2a. 跳过重复的 nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 优化：如果 nums[i] > 0，由于数组已排序，
            # nums[left] 和 nums[right] 也必然 >= nums[i] > 0，
            # 所以它们的和不可能为0。可以直接中断主循环。
            if nums[i] > 0:
                break
            
            # 3. 双指针初始化
            left, right = i + 1, n - 1
            target = -nums[i] # 我们要找 nums[left] + nums[right] == target

            # 4. 移动双指针
            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 4a. 跳过重复的 nums[left] 和 nums[right]
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else: # current_sum > target
                    right -= 1
        
        return ans
# @lc code=end

