#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not (matrix and matrix[0]):
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i*j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    res += dp[i][j]
        return res
# @lc code=end
