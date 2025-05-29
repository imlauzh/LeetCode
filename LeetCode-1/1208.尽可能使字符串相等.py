#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def distance(a, b):
            return abs(ord(a) - ord(b))

        ans = cur_len = 0
        n = len(s)
        l, r = 0, 0
        while r < n:
            maxCost -= distance(s[r], t[r])
            cur_len += 1
            while maxCost < 0 and l < r:
                maxCost += distance(s[l], t[l])
                l += 1
                cur_len -= 1
            if maxCost >= 0:
                ans = max(ans, cur_len)
            r += 1
        return ans

# @lc code=end

