#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
# 暴力解法，左右搜索可以扩展到的位置
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        for i in range(size):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res


# 用单调栈保存递增的值
# 若当前值比栈顶小
# 那么比当前值大的都可以计算有效面积
# 用哨兵可以不用判断空
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        stack=[0]
        n=len(heights)
        res=0
        for i in range(1,n):
            while heights[i]<heights[stack[-1]]:
                currHeight=heights[stack.pop()]
                currWidth=i-stack[-1]-1
                res=max(res,currHeight*currWidth)
            stack.append(i)
        return res


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res
# @lc code=end

