#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, i, j):
            grid2[i][j] = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid2) and 0 <= y < len(grid2[0]) and grid2[x][y] == 1:
                    dfs(grid, x, y)
        
        nc, nr = len(grid1), len(grid1[0])
        res = 0
        for i in range(nc):
            for j in range(nr):
                # 首先将岛屿2与岛屿1没有重叠或有交叉的部分清零
                # 也就是不满足要求的岛屿2
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)
        for i in range(nc):
            for j in range(nr):
                # 再计算清零后的岛屿数量
                if grid2[i][j] == 1:
                    res+=1
                    dfs(grid2, i, j)
        return res
# @lc code=end
