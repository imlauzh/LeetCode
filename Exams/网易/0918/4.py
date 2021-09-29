"""
1
67 69

1
1 100

2
667 669
102 10102
"""


class RealSix:
    def calc(self, a, b):
        def base10(x):
            if x == 100:
                return 2
            if x // 100 > 0:
                return func(x//10)*28
        def func(x):
            if x == 100:
                return 2
            if x % 100 == 0:
                return func(x//10)*8+func(x//10)*20
            digit = 1
            while digit*10 <= x:
                digit *= 10
            high = x//digit*digit

        return func(b)-func(a)
    def calc1(self,a,b):
        if b<68:
            return 0
        else:
            res=0
            for i in range(b-a+1):
                if '8' in str(a+i):
                    for ch in str(a+i):
                        if ch =='6':
                            res+=1
            return res


rs = RealSix()
t = int(input().strip())
for i in range(t):
    a, b = list(map(int, input().strip().split(' ')))
    res = rs.calc1(a, b)
    print(res)
