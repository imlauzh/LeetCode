#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
# 相当于在遍历跳跃次数，统计每次跳跃的起点和最远点
# 如果最远点覆盖了目的点，就说明这一次跳跃就足够，就是最少的跳跃次数
# 把 cur 看作是当前这一“跳跃阶段”的终点。nxt 是在当前这个“跳跃阶段”内探索到的

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        cur, nxt, res = 0, 0, 0
        for i in range(n):
            nxt = max(nxt, i+nums[i])
            if i==cur: # 每次到当前位置都必须跳一步
                res+=1
                cur = nxt
                if nxt>=n-1: 
                    # 为什么这一个判断需要放在这一层？
                    # 因为我们需要在最大可能的范围内搜索：只有当i当前遍历节点到了这一次跳跃的终点时，nxt才是下次一跳跃最远的位置
                    break
        return res
# @lc code=end

