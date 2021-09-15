n,m,q=list(map(int,input().strip().split(' ')))
M=[[0 for _ in range(n)] for i in range(n)]
for i in range(m):
    u,v=list(map(int,input().strip().split(' ')))
    M[u-1][v-1]=M[v-1][u-1]=1

for i in range(q):
    u,v=list(map(int,input().strip().split(' ')))
    r1,r2=M[u-1].copy(),M[v-1].copy()
    for j in range(n):
        if M[u-1][j]==1:
            M[u-1][j]=0
    M[u-1]=list(map(lambda x:x[0]+x[1],zip(r2,M[u-1])))
    for j in range(n):
        if M[v-1][j]==1:
            M[v-1][j]=0
    M[v-1]=list(map(lambda x:x[0]+x[1],zip(r1,M[v-1])))
res=[]
for i in range(n):
    res.append(str(sum(M[i])))
print(" ".join(res))
