#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        ans = inf
        chars = defaultdict(int)
        s_chars = defaultdict(int)
        for c in s:
            s_chars[c] += 1
        for c in "QWER":
            if n // 4 - s_chars[c] < 0:
                chars[c] = n // 4 - s_chars[c]
        need = len(chars)
        # print(chars)
        if need == 0:
            return need
        l, r = 0, 0
        while r < n:
            if s[r] in chars:
                chars[s[r]] += 1
                if chars[s[r]] == 0:
                    need -= 1
            while need == 0 and l <= r:
                # print(l, r, s[l:r+1], chars, need, ans, r-l+1)
                ans = min(ans, r - l + 1)
                if s[l] in chars:
                    if chars[s[l]] == 0:
                        need += 1
                    chars[s[l]] -= 1
                l += 1
            r += 1
        return ans

# @lc code=end

