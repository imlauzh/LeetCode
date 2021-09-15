# Leetcode1004
import bisect


class Length:
    def calc(self,c,k):
        n=len(c)
        helper=[0]
        for i in range(n):
            helper.append(helper[-1]+1-c[i])
        res=0
        for i in range(n):
            index=bisect.bisect_left(helper,helper[i+1]-k)
            res=max(res,i-index+1)
        return res


l=Length()
s=input().strip().split(' ')
k=int(s[1])
c=[int(i) for i in s[0]]
res=l.calc(c,k)
print(res)
