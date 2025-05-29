#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wcnt = 0
        ans = inf
        n = len(blocks)
        for i in range(n):
            if blocks[i] == "W":
                wcnt += 1
            if i < k - 1:
                continue
            ans = min(ans, wcnt)
            if blocks[i - k + 1] == "W":
                wcnt -= 1
        return ans
# @lc code=end

