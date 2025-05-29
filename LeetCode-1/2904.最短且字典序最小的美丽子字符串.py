#
# @lc app=leetcode.cn id=2904 lang=python3
#
# [2904] 最短且字典序最小的美丽子字符串
#

# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        ones = 0
        cur_str = ""
        min_len = inf
        l, r = 0, 0
        while r < n:
            if s[r] == "1":
                ones += 1
            cur_str += s[r]
            while ones >= k and l <= r:
                if ones == k:
                    if len(cur_str) < min_len:
                        ans = cur_str
                        min_len = len(cur_str)
                    elif len(cur_str) == min_len:
                        ans = min(ans, cur_str)
                if s[l] == "1":
                    ones -= 1
                cur_str = cur_str[1:]
                l += 1
            r += 1
        return ans

# @lc code=end

