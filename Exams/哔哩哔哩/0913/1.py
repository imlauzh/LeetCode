"""
锦标赛
时间限制： 3000MS
内存限制： 589824KB
题目描述：
n 名乒乓球单打运动员参加奥运会，所有运动员站成一排，并根据最开始的站位从 1 到 n 编号（运动员 1 是这一排中的第一个运动员，运动员 2 是第二个运动员，依此类推）。

奥运会乒乓球比赛由多个回合组成（从回合 1 开始）。每一回合中，这一排从前往后数的第 i 名运动员需要与从后往前数的第 i 名运动员比拼，获胜者将会进入下一回合。如果当前回合中运动员数目为奇数，那么中间那位运动员将轮空晋级下一回合。

例如，当前回合中，运动员 1, 2, 4, 6, 7 站成一排

运动员 1 需要和运动员 7 比拼

运动员 2 需要和运动员 6 比拼

运动员 4 轮空晋级下一回合

每回合结束后，获胜者将会基于最开始分配给他们的原始顺序（升序）重新排成一排。

众所周知，在乒乓球项目中，中国选手具有碾压世界各国选手的实力。编号为 firstPlayer 和 secondPlayer 的运动员是本届奥运会比赛中的两名中国运动员。在他们开始比拼之前，完全可以战胜任何外国运动员。而任意外国运动员进行比拼时，其中任意一个都有获胜的可能，因此你可以裁定谁是这一回合的获胜者。

给你三个整数 n、firstPlayer 和 secondPlayer。返回一个由两个值组成的整数数组，分别表示两位最佳运动员在本场锦标赛中比拼的最早回合数和最晚回合数。

在输入中:

● 2 <= n <= 28

● 1 <= firstPlayer < secondPlayer <= n

举例1:

输入：

11 2 4

输出：

3 4

解释：

输入为n = 11, firstPlayer = 2, secondPlayer = 4

一种能够产生最早回合数的情景是：

回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

回合 2：2, 3, 4, 5, 6, 11

回合 3：2, 3, 4

一种能够产生最晚回合数的情景是：

回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

回合 2：1, 2, 3, 4, 5, 6

回合 3：1, 2, 4

回合 4：2, 4



输入描述
给你三个整数 n、firstPlayer 和 secondPlayer，数字间空格隔开。

输出描述
返回一个由两个值组成的整数数组，空格隔开，分别表示两位最佳运动员在本场锦标赛中比拼的最早回合数和最晚回合数。

样例输入
11 2 4
样例输出
3 4

https://leetcode-cn.com/problems/the-earliest-and-latest-rounds-where-players-compete/solution/zui-jia-yun-dong-yuan-de-bi-pin-hui-he-b-lhuo/
"""


class Contest:
    def __init__(self, fp, sp):
        self.fp = fp
        self.sp = sp
    
    # tmp1：比赛队员，tmp2：获胜队员，index0, index1：进行比赛的双方
    # round：比赛轮次
    def dfs(self, tmp1, tmp2, index0, index1, round):
        # 一轮完成，进行下一轮
        if index0 > index1:
            self.dfs(sorted(tmp2), [], 0, len(tmp2)-1, round+1)
            return
        # 轮空
        elif index0 == index1:
            self.dfs(tmp1, tmp2+[tmp1[index0]], index0+1, index1-1, round)
            return
        # 两强相遇，更新res
        if (tmp1[index0] == self.fp and tmp1[index1] == self.sp) or (tmp1[index0] == self.sp and tmp1[index1] == self.fp):
            self.res = (min(self.res[0], round), max(self.res[1], round))
        # 碾压
        elif tmp1[index1] == self.fp or tmp1[index1] == self.sp:
            self.dfs(tmp1, tmp2+[tmp1[index1]], index0+1, index1-1, round)
        elif tmp1[index0] == self.fp or tmp1[index0] == self.sp:
            self.dfs(tmp1, tmp2+[tmp1[index0]], index0+1, index1-1, round)
        # 其余都可能获胜，两个分支都走
        else:
            self.dfs(tmp1, tmp2+[tmp1[index0]], index0+1, index1-1, round)
            self.dfs(tmp1, tmp2+[tmp1[index1]], index0+1, index1-1, round)
        return

    def calc(self, n, fp, sp):
        self.res = (float('inf'), float('-inf'))
        tmp1 = [i+1 for i in range(n)]
        tmp2 = []
        self.dfs(tmp1, tmp2, 0, n-1, 1)
        return self.res


n, fp, sp = list(map(int, input().strip().split(' ')))
cont = Contest(fp, sp)
res = cont.calc(n, fp, sp)
print(' '.join(str(i) for i in res))
