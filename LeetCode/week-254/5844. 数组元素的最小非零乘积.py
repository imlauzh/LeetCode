#
# @lc app=leetcode.cn id=5844 lang=python3
#
# [5844] 数组元素的最小非零乘积
#

# @lc code=start
m9 = 10**9+7
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        a = (pow(2, p, m9) - 1)
        b = (pow(2, p, m9) - 2)
        c = pow(2, p-1) - 1
        # print(a,b,c)
        return (a * pow(b, c, m9)) % m9
# @lc code=end
