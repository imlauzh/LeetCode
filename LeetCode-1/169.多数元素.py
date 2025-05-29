#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
# 多数元素
# 暴力：哈希表枚举统计个数排序；排序后取中间数字
# 进阶：同归于尽法

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        winner = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i]==winner:
                count+=1
            else:
                if count==0:
                    winner=nums[i]
                    count+=1
                else:
                    count-=1
        return winner
# @lc code=end

