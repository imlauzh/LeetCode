#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            # 出界，或者不是 '1'，就不再往下递归
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'  # 插旗！避免来回横跳无限递归
            dfs(i, j - 1)  # 往左走
            dfs(i, j + 1)  # 往右走
            dfs(i - 1, j)  # 往上走
            dfs(i + 1, j)  # 往下走

        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '1':  # 找到了一个新的岛
                    dfs(i, j)  # 把这个岛插满旗子，这样后面遍历到的 '1' 一定是新的岛
                    ans += 1
        return ans
# @lc code=end

