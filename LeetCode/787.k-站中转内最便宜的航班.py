#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float('inf')]*n for _ in range(k+2)]
        dp[0][src] = 0
        for t in range(1, k+2):
            for j, i, cost in flights:
                # 经过t个中转站从src到达i城市所需的最小花费为
                # 经过t-1个中转站到达j城市加上j到i的花费
                # 与当前值的最小值
                dp[t][i] = min(dp[t][i], dp[t-1][j]+cost)
        res = min(dp[t][dst] for t in range(1, k+2))
        return -1 if res == float('inf') else res
# @lc code=end
