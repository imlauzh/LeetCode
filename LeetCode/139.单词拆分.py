#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        maxLen = max(len(i) for i in wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(min(i+maxLen,n), i, -1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
# @lc code=end
