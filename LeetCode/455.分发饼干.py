#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        k,c=0,0
        while k<len(g) and c<len(s):
            if s[c]>=g[k]:k+=1
            c+=1
        return k
# @lc code=end

