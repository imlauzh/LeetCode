#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt_p = Counter(p)
        cnt_s = Counter()
        for r, c in enumerate(s):
            cnt_s[c] += 1
            l = r - len(p) + 1
            if l < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(l)
            cnt_s[s[l]] -= 1
        return ans

# @lc code=end

