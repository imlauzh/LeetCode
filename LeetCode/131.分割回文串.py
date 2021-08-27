#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[True]*n for _ in range(n)]
        # dp[i][j]代表s[i:j+1]是否为回文
        # 依赖上一状态s[i+1:j]-->dp[i+1][j-1]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j]=(s[i]==s[j]) and dp[i+1][j-1]
        def backTrack(pos):
            if pos==n:
                res.append(combine[:])
                return
            for i in range(pos,n):
                # 从pos往后搜索回文串
                if dp[pos][i]:
                    combine.append(s[pos:i+1])
                    backTrack(i+1)
                    combine.pop()
        res=[]
        combine=[]
        backTrack(0)
        return res
# @lc code=end

