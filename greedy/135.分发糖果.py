#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, r: List[int]) -> int:
        size=len(r)
        c=[1]*size
        for i in range(1,size):
            if r[i]>r[i-1]:
                c[i]=c[i-1]+1
        for i in reversed(range(1,size)):
            if r[i]<r[i-1]:
                c[i-1]=max(c[i-1],c[i]+1)
        return sum(c)

# @lc code=end

