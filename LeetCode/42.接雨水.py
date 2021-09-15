#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#

# 动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        leftMax, rightMax = [0]*n, [0]*n
        leftMax[0], rightMax[-1] = height[0], height[-1]
        for i in range(0, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(n-2, 0, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        dp = [0]*n
        for i in range(n):
            dp[i] = max(min(leftMax[i], rightMax[i])-height[i], 0)
        print(leftMax)
        print(rightMax)
        print(dp)
        return sum(dp)


# O(n), O(1)
# 双指针，优化空间复杂度
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                res += leftMax-height[left]
                left += 1
            else:
                res += rightMax-height[right]
                right -= 1
        return res


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                res += leftMax-height[left]
                left += 1
            else:
                res += rightMax-height[right]
                right -= 1
        return res
# @lc code=end
