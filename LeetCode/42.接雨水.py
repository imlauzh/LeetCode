#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (56.14%)
# Likes:    2493
# Dislikes: 0
# Total Accepted:    275.3K
# Total Submissions: 487K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 0
# 0
#
#
#

# 动态规划
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n<3:
            return 0
        leftMax, rightMax = [0]*n, [0]*n
        leftMax[0],rightMax[-1]=height[0],height[-1]
        for i in range(0,n):
            leftMax[i]=max(leftMax[i-1],height[i])
        for i in range(n-2,0,-1):
            rightMax[i]=max(rightMax[i+1],height[i])
        dp=[0]*n
        for i in range(n):
            dp[i]=max(min(leftMax[i],rightMax[i])-height[i],0)
        print(leftMax)
        print(rightMax)
        print(dp)
        return sum(dp)

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<3:return 0
        left_max=[0]*n
        right_max=[0]*n
        left_max[0],right_max[-1]=height[0],height[-1]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i])
        dp=[0]*n
        for i in range(n):
            dp[i]=max(min(left_max[i],right_max[i])-height[i],0)
        return sum(dp)
# @lc code=end
