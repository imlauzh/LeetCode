#
# min edit cost
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @param ic int整型 insert cost
# @param dc int整型 delete cost
# @param rc int整型 replace cost
# @return int整型
#
class Solution:
    def minEditCost(self, str1, str2, ic, dc, rc):
        # write code here
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = ic*i
        for i in range(m+1):
            dp[i][0] = dc*i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+dc, dp[i]
                                   [j-1]+ic, dp[i-1][j-1]+rc)
        return dp[-1][-1]
