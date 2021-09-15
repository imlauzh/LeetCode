#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        add = 0
        res = []
        while i >= 0 or j >= 0 or add > 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            ans = x+y+add
            res.append(str(ans % 10))
            add = ans//10
            i -= 1
            j -= 1
        return ''.join(res[::-1])
# @lc code=end
