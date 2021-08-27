#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
# 双指针，先判断是不是子串，再排序找最长且字典序最小的

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubstring(x, y):
            i, j = 0, 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    j += 1
                i += 1
            return j == len(y)
        res = ""
        for str in dictionary:
            if isSubstring(s, str):
                if len(str) > len(res) or (len(str) == len(res) and str < res):
                    res = str
        return res
# @lc code=end
