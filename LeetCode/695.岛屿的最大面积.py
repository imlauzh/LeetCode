#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            res = 0
            res += grid[i][j]
            visited[i][j] = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and visited[x][y] == 0:
                    res += dfs(x, y)
            return res
        nr, nc = len(grid), len(grid[0])
        visited = [[0]*nc for _ in range(nr)]
        res = 0
        for i in range(nr):
            for j in range(nc):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
# @lc code=end
