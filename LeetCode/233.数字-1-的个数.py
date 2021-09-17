#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
# 规律
class Solution:
    def countDigitOne(self, n: int) -> int:
        mulk = 1
        res = 0
        while n >= mulk:
            res += (n//(mulk*10))*mulk+min(max(n % (mulk*10)-mulk+1, 0), mulk)
            mulk *= 10
        return res


# 递归
class Solution:
    def countDigitOne(self, n: int) -> int:
        def dfs(num):
            if num <= 0:
                return 0
            digit = 1
            while digit*10 <= num:
                digit *= 10
            highest = num//digit
            low = num % digit
            if highest == 1:
                return (low+highest)+dfs(digit-1)+dfs(low)
            else:
                return digit+highest*dfs(digit-1)+dfs(low)
        return dfs(n)


# @lc code=start
class Solution:
    def countDigitK(self, n, k):
        res = 0
        digit = 1
        while digit <= n:
            high = n//digit//10
            curr = (n//digit) % 10
            low = n % 10
            if k != 0:
                if curr > k:
                    res += (high+1)*digit
                elif curr == k:
                    res += high*digit+low+1
                else:
                    res += high*digit
            else:
                if curr == 0:
                    res += (high-1)*digit+low+1
                else:
                    res += high*digit
            digit *= 10
        return res

    def countDigitOne(self, n: int) -> int:
        return self.countDigitK(n, 1)
# @lc code=end
