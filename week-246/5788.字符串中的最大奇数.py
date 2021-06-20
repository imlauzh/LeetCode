#
# @lc app=leetcode.cn id=5788 lang=python3
#
# [5788] 字符串中的最大奇数
# Accepted
# 196/196 cases passed (280 ms)
# Your runtime beats 50 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (15.5 MB)

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx=-1
        for i in range(len(num)):
            if int(num[i])%2!=0:
                idx=i
        if idx==-1:return ""
        else:return num[:idx+1]
# @lc code=end

