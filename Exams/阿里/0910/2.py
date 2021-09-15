"""
逆池化
1 2 3 4
3
1 1
4 5
1 4
"""
A, B, C, D = list(map(int, input().strip().split(' ')))
q = int(input().strip())


def getNum(x, y):
    if x == 1:
        return A if y == 1 else B
    else:
        return D if y == 1 else C


def calc(x, y):
    start = 2
    while max(x, y) > start:
        start *= 2
    mid = start//2
    if mid == 1:
        return getNum(x, y)
    if x > mid:
        if y > mid:
            return C+calc(x-mid, y-mid)
        else:
            return D+calc(x-mid, y)
    else:
        if y > mid:
            return B+calc(x, y-mid)
        else:
            return getNum(x, y)


for i in range(q):
    x, y = list(map(int, input().strip().split(' ')))
    print(calc(x, y))
