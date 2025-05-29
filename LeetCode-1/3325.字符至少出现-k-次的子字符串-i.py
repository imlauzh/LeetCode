#
# @lc app=leetcode.cn id=3325 lang=python3
#
# [3325] 字符至少出现 K 次的子字符串 I
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        max_cnt, max_char = 0, ""
        ocrr = defaultdict(int)
        l, r = 0, 0
        while r < n:
            ocrr[s[r]] += 1
            if ocrr[s[r]] > max_cnt:
                max_cnt = ocrr[s[r]]
                max_char = s[r]
            while max_cnt >= k:
                ocrr[s[l]] -= 1
                if s[l] == max_char:
                    max_char, max_cnt = max(ocrr.items(), key=lambda x: x[1])
                l += 1
            ans += l
            r += 1
        return ans
# @lc code=end


# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        ocrr = defaultdict(int)
        l, r = 0, 0
        while r < n:
            ocrr[s[r]] += 1
            while ocrr[s[r]] >= k:
                ocrr[s[l]] -= 1
                l += 1
            ans += l
            r += 1
        return ans
# @lc code=end