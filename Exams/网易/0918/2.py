"""
1
3 3 2 3 2 1

3
1 3 2 1 2 3
1 2 3 1 2 3
3 3 3 1 2 3
"""
class DirtySequence:
    def calc(self,A,B,C,x,y,z):
        return -1


ds=DirtySequence()
t=int(input().strip())
for i in range(t):
    A,B,C,x,y,z=list(map(int,input().strip().split(' ')))
    res=ds.calc(A,B,C,x,y,z)
    print(res)
