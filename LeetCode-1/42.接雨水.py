#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
# 核心思想：左右最高的最低高度-当前高度

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        先遍历一遍，统计好左右最高数组
        """
        n = len(height)
        max_lefts = [height[0]] * n
        max_rights = [height[-1]] * n
        for i in range(1, n):
            max_lefts[i] = max(max_lefts[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            max_rights[i] = max(max_rights[i + 1], height[i])
        ans = 0
        for i in range(n):
            ans += min(max_lefts[i], max_rights[i]) - height[i]
        return ans
# @lc code=end


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        一个位置能存的雨水，是由它左右两边较矮的那个墙决定的。
        """
        n = len(height)
        ans = 0
        l, r = 0, n - 1
        lm, rm = 0, 0
        while l < r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])
            if height[l] < height[r]:
                ans += lm - height[l]
                l += 1
            else:
                ans += rm - height[r]
                r -= 1
        return ans
# @lc code=end