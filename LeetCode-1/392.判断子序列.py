#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p0, p1 = 0, 0
        n0, n1 = len(s), len(t)
        while p0<n0 and p1<n1:
            if s[p0]==t[p1]:
                p0+=1
                p1+=1
            else:
                p1+=1
        if p0==n0:
            return True
        if p1==n1:
            return False
# @lc code=end

