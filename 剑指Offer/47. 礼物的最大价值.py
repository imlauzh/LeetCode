class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        dp = [[0]*(nc) for _ in range(nr)]
        dp[0][0] = grid[0][0]
        for i in range(nr):
            for j in range(nc):
                if i+j == 0:
                    continue
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]


# 优化
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if i+j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):  # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):  # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
