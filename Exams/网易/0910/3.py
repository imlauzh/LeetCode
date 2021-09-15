# 2 2
# 飞机座舱
# ***|_|.*.
# **.|_|***

class Solution:
    def fun(self,c):
        def check(i, j):
            for a, b in [(i - 1, j - 1), (i - 1, j), (i + 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                         (i + 1, j + 1)]:
                if 0 <= a < N and 0 <= b < 7:

                    if matrix[a][b] == "com":
                        return False
            return True
        def dfs(temp,c):
            if c==0:
                self.ans= temp[:]
            for i in range(N):
                for j in range(7):
                    if j==3:
                        continue
                    if matrix[i][j]==".":
                        if check(i,j):
                            matrix[i][j] = "com"
                            temp.append((i,j))
                            c-=1
                            dfs(temp,c)
                            matrix[i][j] = "."
                            temp.pop()
                            c+=1
        self.ans = []
        dfs([],c)
        return self.ans

matrix = []
N,C = map(int,input().strip().split(" "))
for i in range(N):
    t = list(input().strip())
    matrix.append(t[0:3]+["*"]+t[-3:])
solution = Solution()
ans = solution.fun(C)
# print(ans)
ch = {0:'A',1:'B',2:'C',4:'D',5:'E',6:'F'}
if ans:
    print("SUCCESS")
    for a in ans:
        row = str(a[0]+1)
        col = ch[a[1]]
        print("".join([row,col]))
else:
    print("FAILED")