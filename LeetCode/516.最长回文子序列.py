#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
# 初始化动态规划数组：因为长度为1的字符串肯定是回文的
# dp[i][j]为序列i到j的最长回文序列
# 如果s[i],s[j]为相同字符
# 那么dp[i][j]为dp[i+1][j-1]+2
# 如果不同,等于前两个状态中取最大


# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        # 最终状态为dp[0][n-1]
        # 所以需要注意循环的顺序
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    # 等于前一个状态
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
# @lc code=end
