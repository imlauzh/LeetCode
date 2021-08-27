#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        res = 0
        for i in range(n):
            # res比当前剩下的点多或者多于一半的点可以直接退出
            # 当前就是最大值
            if res >= n-i or res > n//2:
                break
            # 斜率字典
            slopes = dict()
            for j in range(i+1, n):
                # 计算两个维度的偏移量
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0:
                    # 斜率不存在，保存x轴截距
                    slope = 'x'+str(points[i][0])
                elif y == 0:
                    # 斜率==0，保存y轴截距
                    slope = 'y'+str(points[i][1])
                else:
                    # 确保x为正，避免斜率为‘-1/2’和‘1/-2’时，判断为不共线
                    if x < 0:
                        x, y = -x, -y
                    # 最大公约数
                    gcdNumber = math.gcd(x, y)
                    x, y = x//gcdNumber, y//gcdNumber
                    slope = str(y)+'/'+str(x)
                if slope in slopes:
                    slopes[slope] += 1
                else:
                    # 不存在该斜率，则新增，初始化为2，代表该直线上有2个点
                    slopes[slope] = 2
            res = max(res, max(list(slopes.values())))
        return res
# @lc code=end
