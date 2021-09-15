# 时间限制： 3000MS
# 内存限制： 1048576KB
# 题目描述：
#        又到了一学期一次的大学生期末考试。但很多人期末考试的卷面成绩是不能及格的，需要靠较高的平时成绩来拖上去。平时成绩与期末考试的占比已经确定，假设平时成绩占比为p，期末考试占比为q，平时分为a，期末考试分数为b，则总成绩为(p*a+q*b)/100。（平时分与期末成绩都是整数，但总成绩可以是小数。）

#        饶老师心肠特别好，他希望自己的学生及格率尽可能的高。但他也坚持期末考试分数更高的学生平时成绩也一定要更高。饶老师想知道在这种情况下，他们班的最大及格人数是多少（及格是指总成绩不低于60分）。


# 输入描述
# 第一行三个正整数n，p，q（1<=n<=200,0<=p<=100,0<=q<=100,p+q=100）

# 第二行n个正整数表示n个学生的期末考试分数（0<=分数<=100）

# 输出描述
# 仅一行，一个正整数，表示最大及格人数。
# 4 20 80
# 51 50 50 50
class Solution:
    def maxCount(self, n, p, q, scores):
        scores.sort(reverse=True)
        norm = [100]*n
        for i in range(1, n):
            if scores[i] < scores[i-1]:
                norm[i] = norm[i-1]-1
            elif scores[i] == scores[i-1]:
                norm[i] = norm[i-1]
        c = 0
        for i in range(n):
            norm[i] = p*norm[i]+q*scores[i]
            norm[i] /= 100
            if norm[i] >= 60:
                c += 1
        return c


s = Solution()
ps = input().strip()
ps = list(map(int, ps.split(' ')))
n, p, q = ps[0], ps[1], ps[2]
ss = input().strip()
scores = list(map(int, ss.split(' ')))
res = s.maxCount(n, p, q, scores)
print(res)
