#
# @lc app=leetcode id=1969 lang=python3
#
# [1969] Minimum Non-Zero Product of the Array Elements
#

# @lc code=start
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod9 = 10**9+7
        tmp = pow(2, p)-1
        return tmp*pow(tmp-1, pow(2, p-1)-1, mod9) % mod9
# @lc code=end
