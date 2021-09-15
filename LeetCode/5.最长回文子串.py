#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
# 双指针搜索当前位置为中心的最长回文串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(s, i, j):
            n = len(s)
            while 0 <= i < n and 0 <= j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        n = len(s)
        res = ''
        for i in range(n):
            sub1 = search(s, i, i)
            sub2 = search(s, i, i+1)
            res = sub1 if len(sub1) > len(res) else res
            res = sub2 if len(sub2) > len(res) else res
        return res

        
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(s, i, j):
            n = len(s)
            while 0 <= i < n and 0 <= j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        n = len(s)
        res = ''
        for i in range(n):
            sub1 = search(s, i, i)
            sub2 = search(s, i, i+1)
            res = sub1 if len(sub1) > len(res) else res
            res = sub2 if len(sub2) > len(res) else res
        return res
# @lc code=end
