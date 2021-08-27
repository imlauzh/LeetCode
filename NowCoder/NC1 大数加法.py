#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self, s, t):
        # write code here
        maxLen = max(len(s), len(t))
        s = s.zfill(maxLen)
        t = t.zfill(maxLen)
        carry = 0
        res = ""
        for i in range(maxLen-1, -1, -1):
            last = ord(s[i])+ord(t[i])-2*ord('0')+carry
            carry = last//10
            last = last % 10
            res += str(last)
        if carry:
            res += str(carry)
        return res[::-1]
