#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        def dfs(g, i, j):
            g[i][j] = 0
            m, n = len(g), len(g[0])
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and g[x][y] == "1":
                    dfs(g, x, y)
        ret = 0
        m = len(g)
        n = len(g[0])
        for i in range(m):
            for j in range(n):
                if g[i][j] == "1":
                    ret += 1
                    dfs(g, i, j)
        return ret
# @lc code=end
