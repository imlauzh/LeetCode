# 时间限制： 3000MS
# 内存限制： 1048576KB
# 题目描述：
#        长城上有连成一排的n个烽火台，每个烽火台都有士兵驻守。

#        第i个烽火台驻守着ai个士兵，相邻峰火台的距离为1。另外，有m位将军，每位将军可以驻守一个峰火台，每个烽火台可以有多个将军驻守，将军可以影响所有距离他驻守的峰火台小于等于x的烽火台。每个烽火台的基础战斗力为士兵数，另外，每个能影响此烽火台的将军都能使这个烽火台的战斗力提升k。长城的战斗力为所有烽火台的战斗力的最小值。

#        请问长城的最大战斗力可以是多少？



# 输入描述
# 第一行四个正整数n,m,x,k(1<=x<=n<=10^5,0<=m<=10^5,1<=k<=10^5)

# 第二行n个整数ai(0<=ai<=10^5)

# 输出描述
# 仅一行，一个整数，表示长城的最大战斗力
# 5 2 1 2
# 4 4 2 4 4
class Solution:
    def maxCount(self, n, m, x, k, a):
        



s = Solution()
line0 = input().strip()
line0 = list(map(int, line0.split(' ')))
n, m, x, k = line0[0], line0[1], line0[2], line0[3]
line1 = input().strip()
a = list(map(int, line1.split(' ')))
res = s.maxCount(n, m, x, k, a)
print(res)