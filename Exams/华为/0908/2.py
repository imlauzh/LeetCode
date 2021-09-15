"""
题目：给定一个M * N的梅花桩阵，每个桩都有允许跳跃的最大步数，用户用0，0位置开始跳跃。允许向右和向下两个方向跳跃，求最少需要跳跃多少次能达到M-1, N-1的位置，无法达到目的地时候返回-1.其中M<=100,N<=100,每个桩上允许跳跃的最大步数均为小于10的正整数。0表示不允许跳跃到该位置。
输入描述：第一行为M，N，用“，”隔开，
第二行为M*N的梅花桩阵，（格式如样例）数组位置为允许跳跃的最大步数，0表示改位置为空，不允许跳到该位置。
输出描述：最少跳跃的步数。
示例 输入
3,3
3 2 2 0 1 0 1 1 1
输出
2
"""
class Meihua:
    def calc(self, sticks):
        seen = dict()

        def dp(i, j, seen):
            if i == m-1 and j == n-1:
                return 0
            if sticks[i][j] == 0:
                return float('inf')
            if (i, j) in seen:
                return seen[(i, j)]
            res = float('inf')
            for k in range(1, sticks[i][j]+1):
                if j+k <= n-1:
                    res = min(res, 1+dp(i, j+k, seen))
                if i+k <= m-1:
                    res = min(res, 1+dp(i+k, j, seen))
            seen[(i, j)] = res
            return res
        return dp(0, 0, seen)


mh = Meihua()
m, n = list(map(int, input().strip().split(',')))
nums = list(map(int, input().strip().split(' ')))
sticks = []
for i in range(0, m*n, n):
    sticks.append(nums[i:i+n])
res = mh.calc(sticks)
print(res)
