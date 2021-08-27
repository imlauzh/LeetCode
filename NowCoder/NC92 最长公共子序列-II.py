#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, s1, s2):
        # write code here
        m, n = len(s1), len(s2)
        if n == 0 or m == 0:
            return -1
        dp = [[""]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+s1[i-1]
                else:
                    dp[i][j] = dp[i -
                                  1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
        return dp[m][n] if len(dp[m][n]) > 0 else "-1"
