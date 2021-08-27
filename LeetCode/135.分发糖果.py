#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        ret=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                ret[i]=max(ret[i],ret[i-1]+1)
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                ret[i]=max(ret[i],ret[i+1]+1)
        print(ret)
        return sum(ret)
# @lc code=end

