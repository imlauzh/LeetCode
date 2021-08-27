#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, j):
            isConnected[i][j] = 0
            for x in range(len(isConnected[0])):
                if isConnected[x][j] == 1:
                    dfs(x, j)
            for y in range(len(isConnected[0])):
                if isConnected[i][y] == 1:
                    dfs(i, y)
        n = len(isConnected)
        res = 0
        for i in range(n):
            isConnected[i][i] == 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res += 1
                    dfs(i, j)
        return res
# @lc code=end
