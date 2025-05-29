#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                while l + 1 < r and s[l] == s[l + 1]:
                    l += 1
                while l < r - 1 and s[r] == s[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            else:
                break
        return r - l + 1

# @lc code=end

