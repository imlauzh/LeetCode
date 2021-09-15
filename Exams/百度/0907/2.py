# 小明的店里准备了一些礼物，分为a，b两个品种。为了促销，小明希望把礼物进行组合后打包售卖。组合的方式包括两种，一种是组合里有x件a类礼物加y件b类礼物，一种是组合里有x件b类礼物加y件a类礼物。小明希望自己的组合数越多越好，你能告诉他他最多可以组多少个组合么？

# 一行四个空格隔开的整数a,b,x,y，分别表示a类礼物的数量，b类礼物的数量，组合要求的x和y的大小，1<=a,b,x,y<=1000000000

# 一个整数，表示最大组合数量。

# 10 12 2 5
# 3

class Gifts:
    def calc(self, a, b, x, y):
        res = 0
        minxy, maxxy = min(x, y), max(x, y)
        minab, maxab = min(a, b), max(a, b)
        while minab >= minxy and maxab >= maxxy:
            minab -= minxy
            maxab -= maxxy
            res += 1
            minab, maxab = min(minab, maxab), max(minab, maxab)
        return res


g = Gifts()
a, b, x, y = list(map(int, input().strip().split(' ')))
res = g.calc(a, b, x, y)
print(res)
