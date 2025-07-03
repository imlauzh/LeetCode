#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        ans = []
        path = [""] * m

        def dfs(i: int, open: int) -> None:
            if i == m:
                ans.append("".join(path))
                return
            if open < n:
                path[i] = "("
                dfs(i + 1, open + 1)
            if i - open < open:
                path[i] = ")"
                dfs(i + 1, open)

        dfs(0, 0)
        return ans


# @lc code=end

