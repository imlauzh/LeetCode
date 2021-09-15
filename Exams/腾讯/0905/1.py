def calc(i,j,q):
    if i==1 or j==1 :
        return i==q
    res=1
    while res<=q and j>0:
        if j%2:
            res*=i
        j//=2
        i*=i
    if res ==q and j==0 :
        True
    return False

def calc2(a,q):
    for i in range(len(a)):
        

line=input().strip().split(' ')
line=list(map(int,line))
n,m=line
a=input().strip().split(' ')
a=list(map(int,a))
b=input().strip().split(' ')
b=list(map(int,b))
