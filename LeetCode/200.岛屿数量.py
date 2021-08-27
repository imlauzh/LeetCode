#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            self.visited[i][j] = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and self.visited[x][y] == 0 and grid[x][y] == '1':
                    dfs(x, y)
        nr, nc = len(grid), len(grid[0])
        self.visited = [[0]*nc for _ in range(nr)]
        res = 0
        for i in range(nr):
            for j in range(nc):
                if self.visited[i][j] == 0 and grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
# @lc code=end
