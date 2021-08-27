#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
# 前期先积累汽油，后期消耗
# 也就是从消耗最多的下一个加油站出发
# 让到达该车站前多积累汽油
# 最小前缀和的思想


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minL, currL = 1e10, 0
        n = len(gas)
        ret = 0
        for i in range(n):
            currL += gas[i]-cost[i]
            if currL < minL:
                ret = i
                minL = currL
        return (ret+1) % n if currL >= 0 else -1
# @lc code=end
