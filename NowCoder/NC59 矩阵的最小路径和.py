#
#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self, matrix):
        # write code here
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = matrix[0][0]
        for i in range(1, n):
            dp[0][i] = matrix[0][i]+dp[0][i-1]
        for i in range(1, m):
            dp[i][0] = matrix[i][0]+dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+matrix[i][j]
        return dp[-1][-1]
