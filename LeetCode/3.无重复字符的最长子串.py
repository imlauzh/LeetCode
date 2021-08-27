#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (37.33%)
# Likes:    5763
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
# 提示：
#
#
# 0
# s 由英文字母、数字、符号和空格组成
#
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk-i+1)
        return ans


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res, n, j = 0, len(s), -1
        for i in range(n):
            if i != 0:
                seen.remove(s[i-1])
            while j+1 < n and s[j+1] not in seen:
                j += 1
                seen.add(s[j])
            res = max(res, j-i+1)
        return res
# @lc code=end
