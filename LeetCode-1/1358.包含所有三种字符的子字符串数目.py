#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        ocrr = defaultdict(int)
        n = len(s)
        l, r = 0, 0
        while r < n:
            ocrr[s[r]] += 1
            while len(ocrr) == 3:
                ocrr[s[l]] -= 1
                if ocrr[s[l]] == 0:
                    del ocrr[s[l]]
                l += 1
            ans += l
            r += 1
        return ans

# @lc code=end

