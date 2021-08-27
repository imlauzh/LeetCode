#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
# 动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = ' '+s
        f = [0]*(n+1)
        f[0] = 1
        for i in range(1, n+1):
            a=ord(s[i])-ord('0')
            b=(ord(s[i-1])-ord('0'))*10+a
            print(ord(' ')-ord('0'))
            if 1<=a<=9:
                f[i]+=f[i-1]
            if 10<=b<=26:
                f[i]+=f[i-2]
        return f[n]


# 空间优化
# 不难发现，我们转移 f[i] 时只依赖 f[i-1] 和 f[i-2] 两个状态。
# 因此我们可以采用与「滚动数组」类似的思路，只创建长度为 3 的数组，通过取余的方式来复用不再需要的下标。
# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = ' ' + s
        f = [0] * 3
        f[0] = 1
        for i in range(1,n + 1):
            f[i % 3] = 0
            a = ord(s[i]) - ord('0')
            b = ( ord(s[i - 1]) - ord('0') ) * 10 + ord(s[i]) - ord('0')
            if 1 <= a <= 9:
                f[i % 3] = f[(i - 1) % 3]
            if 10 <= b <= 26:
                f[i % 3] += f[(i - 2) % 3]
        return f[n % 3]
# @lc code=end
