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
        low, high, ans = 0, x, -1
        while low <= high:
            mid = low+(high-low)//2
            if mid**2 <= x:
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans


# 牛顿法，f(x)=x^2-a=0
# 下一个近似值等于当前值减去函数值比上梯度：
# x_{n+1}=x_n-f(x_n)/f(x_n)'
# 函数的梯度为2x，那么把f(x)=x^2-a带入上式
# x-(x^2-a)/2x ==> (x+a/x)/2
# 注意这里的x, a分别对应参数res, x
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        while a**2 > x:
            a = int(a+x/a)//2
        return a
# @lc code=end
