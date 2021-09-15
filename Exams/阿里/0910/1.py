# 先确定谁大谁小。让小的值一直加，直到大于等于较大值
# 求两者的差值，如果差值为偶数则直接返回加的次数
# 如果差值是奇数，则继续加，直到差值是偶数为止，返回次数
# 因为加k或减去k之间的差值都是偶数，2，4，6，8，……
# 所以如果差值是偶数，直接返回即可
class Nature:
    def calc(self, a, b):
        extra = abs(b-a)
        tmp = 1
        k = 1
        while k < extra:
            tmp += 1
            k += tmp
        if k == extra:
            res = tmp
        elif (k-extra) % 2 == 0:
            res = tmp
        else:
            while (k-extra) % 2 != 0:
                tmp += 1
                k += tmp
            res = tmp
        return res


nat = Nature()
t = int(input().strip())
for i in range(t):
    a, b = list(map(int, input().strip().split(' ')))
    res = nat.calc(a, b)
    print(res)
