"""
3
5 1 5
"""
class Sequence:
    def calc(self, n, s):
        res = 0
        if n > 2:
            s.sort()
            largest = [s[-1]]
            s.pop(-1)
            tmp = 1
            while s:
                if len(s) == 1:
                    if tmp == 1:
                        largest.insert(0, s[0])
                        break
                    else:
                        largest.append(s[0])
                        break
                if tmp == 1:
                    largest.insert(0, s[0])
                    s.pop(0)
                    largest.append(s[0])
                    s.pop(0)
                    tmp = 0
                else:
                    largest.insert(0, s[-1])
                    s.pop(-1)
                    largest.append(s[-1])
                    s.pop(-1)
                    tmp = 1

            if abs(largest[-1]-largest[-2]) < abs(largest[0]-largest[-1]):
                temp = largest[-1]
                largest.pop()
                largest.insert(0, temp)

            for x in range(n-1):
                res += abs((largest[x+1]-largest[x]))

        elif n == 2:
            res = abs(s[0]-s[1])

        return res


seq = Sequence()
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
res = seq.calc(n, s)
print(res)
