#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left,right=0,len(height)-1
        while left<right:
            if height[left]<=height[right]:
                res=max(res,height[left]*(right-left))
                left+=1
            else:
                res=max(res,height[right]*(right-left))
                right-=1
        return res
# @lc code=end
