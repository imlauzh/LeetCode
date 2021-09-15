# class SSR:
#     def calcProb(self, n, m):
#         q = n/(n+1)
#         k = 1000
#         s1 = -2/(n+1)
#         s2 = -((q**k-q)/(q-1))/(n+1)
#         s3 = ((n/(n+1))**k)/(n+1)*k
#         return -(s1+s2+s3)*m*(n+1)


# ssr = SSR()
# line = input().strip().split(' ')
# line = list(map(int, line))
# n, m = line
# res = ssr.calcProb(n, m)
# print(format(res, '.2f'))


class SSR:
    def calcProb(self, n, m):
        # q = n/(n+1)
        # k = 1000
        # s1=-2/(n+1)
        # s2=-((q**k-q)/(q-1))/(n+1)
        # s3=((n/(n+1))**k)/(n+1)*k
        # return -(s1+s2+s3)*m*(n+1)
        res = 0
        while m > 0:
            res += float(n+m)/float(m)+1
            m -= 1
        return float(res)


ssr = SSR()
line = input().strip().split(' ')
line = list(map(int, line))
n, m = line
res = ssr.calcProb(n, m)
print(format(res, '.2f'))
