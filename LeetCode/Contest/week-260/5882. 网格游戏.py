# 只需要保证第二个机器人的点数和可能的最大值最小即可
# 根据第一个机器人向下的位置
# 第二个机器人可以获得的点数就是右上角或者是左下角
# 那么分别计算不同向下位置时，两个区域和的最小值即可
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        # r1右上角区域
        # r2左下角区域
        r1, r2 = [0]*n, [0]*n
        # 前缀和计算
        for i in range(n-1, 0, -1):
            r1[i-1] = r1[i]+grid[0][i]
        for i in range(n-1):
            r2[i+1] = r2[i]+grid[1][i]
        res = float('inf')
        for i in range(n):
            res = min(res, max(r1[i], r2[i]))
        return res
