#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b=0,int(sqrt(c))
        while a<=b:
            if a**2+b**2==c:
                return True
            elif a**2+b**2<c:
                a+=1
            else:
                b-=1
        return False
# @lc code=end

