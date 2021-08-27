#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (28.79%)
# Likes:    3652
# Dislikes: 157
# Total Accepted:    189.5K
# Total Submissions: 658.3K
# Testcase Example:  '"1432219"\n3'
#
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
# 
# 
# Example 1:
# 
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# Example 2:
# 
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# Example 3:
# 
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= num.length <= 10^5
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 数字长度小于删除的位数直接输出0
        if len(num)<=k:
            return "0"
        stack=[]
        for i in num:
            # 当前值i比栈顶小，且还可以移除数字，把栈顶pop
            # 构造一个非递减的序列，也就是数字开始值最小
            while k and stack and stack[-1] > i:
                stack.pop()
                k-=1
            stack.append(i)
        # 如果k大于0，那么就只保留前面的数字
        ret=stack[:-k] if k else stack
        # 去除前导0，如果数字是空字符串，返回’0‘
        return ''.join(ret).lstrip('0') or '0'
# @lc code=end

