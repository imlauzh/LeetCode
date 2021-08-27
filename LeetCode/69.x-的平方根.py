#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
# math法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5*math.log(x)))
        return ans+1 if (ans+1)**2 <= x else ans


# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l+r)//2
            if mid**2 <= x:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans


# 牛顿法，f(x)=x^2-a=0
# x_{n+1}=x_n-f(x_n)/f(x_n)'
# x_{n+1}=(x_n+a/x_n)/2
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        a=x
        while a**2>x:
            a=int(a+x/a)//2
        return a
# @lc code=end
