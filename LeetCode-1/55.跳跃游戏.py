#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
# 
# 直接遍历所有点，如果当前点比前面所有点可以达到的点的最大距离还要大就返回false，如果能遍历到最后一个点，说明最后一个点可以到达，返回true

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k=0
        for i in range(len(nums)):
            if i>k: return False
            k = max(k, i+nums[i])
        return True
# @lc code=end

