"""
reward计算
"""
class Game:
    def calc(self, n, m, a, reward, x, y):
        def mul(l1,l2):
            res=0
            for i in range(len(l1)):
                res+=l1[i]*l2[i]
            return res
        res = []
        aa=[0]*n
        for i in range(n):
            aa[i]=a**i
        for i in range(m):
            xi, yi = x[i], y[i]
            tmp = mul(aa[:yi-xi+1],reward[xi:yi+1])
            res.append(int(tmp))
        return res


game = Game()
n, m, a = 5, 15, 0.95
reward = [80000, 13000, 21000, 34000, 55000]
x, y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4], [
    4, 3, 2, 1, 0, 4, 3, 2, 1, 4, 3, 2, 4, 3, 4]
res = game.calc(n, m, a, reward, x, y)
print(res)
