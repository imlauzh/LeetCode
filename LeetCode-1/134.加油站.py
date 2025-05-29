#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
# 从剩的最多的开始
# 剩的最少的节点最后访问

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas_left = [gas[i]-cost[i] for i in range(n)]
        if sum(gas_left)<0:
            return -1
        print(gas_left)
        start = -1 # 初始状态
        cur_gas_left = 0
        for i in range(n):
            if cur_gas_left + gas_left[i] < 0: # 当前节点加上后到不了下一个，重置
                start=-1
                cur_gas_left = 0
            else: # 可以到下一个
                if start==-1: # 初始状态，使用当前节点
                    start = i
                cur_gas_left += gas_left[i]
        return start
# @lc code=end

