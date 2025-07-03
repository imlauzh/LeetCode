#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int) -> None:
            d = k - len(path)
            if t < 0 or t > (i * 2 - d + 1) * d // 2:
                return
            if d == 0 and t == 0:
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()

        dfs(9, n)
        return ans

# @lc code=end

