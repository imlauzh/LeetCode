#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = cnt = 0
        n = len(s)
        chars = defaultdict(int)
        l, r = 0, 0
        while r < n:
            chars[s[r]] += 1
            cnt += 1
            while chars[s[r]] > 2:
                chars[s[l]] -= 1
                cnt -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            ans = max(ans, cnt)
            r += 1
        return ans

# @lc code=end

