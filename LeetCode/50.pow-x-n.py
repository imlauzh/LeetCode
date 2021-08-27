#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
# 二分快速幂，递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(x, n):
            if n == 0:
                return 1.0
            y = quickMul(x, n//2)
            return y*y if n % 2 == 0 else y*y*x
        return quickMul(x, n) if n >= 0 else 1.0/quickMul(x, -n)


# 快速幂，迭代
# 幂转化成二进制，那么x^n-->x^{1001101}-->x^{2^6+2^3+2^2+2^0}
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(x, n):
            ans = 1.0
            xPow = x
            while n > 0:
                if n % 2 == 1:
                    ans *= xPow
                xPow *= xPow
                n //= 2
            return ans
        return quickMul(x, n) if n >= 0 else 1.0/quickMul(x, -n)


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(x, n):
            ans = 1.0
            xPow = x
            while n > 0:
                if n % 2 == 1:
                    ans *= xPow
                xPow *= xPow
                n //= 2
            return ans
        return quickMul(x, n) if n >= 0 else 1.0/quickMul(x, -n)
# @lc code=end
