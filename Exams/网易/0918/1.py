"""
4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4

8
-1 2 14 7 4 -5 8 9
10 6 23 2 -1 -1 7 11
9 3 5 -2 4 4 6 6
7 15 0 8 21 20 6 6
19 8 12 -8 4 5 2 9
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
"""


class Pooling:
    def calc(self, n, matrix):
        while True:
            curr = len(matrix)
            if curr != 1:
                mmatrix = []
                for i in range(0, curr-1, 2):
                    tmp1 = []
                    for j in range(0, curr-1, 2):
                        tmp2 = [matrix[i][j], matrix[i][j+1],
                                matrix[i+1][j], matrix[i+1][j+1]]
                        tmp2 = sorted(tmp2)
                        tmp1.append(tmp2[-2])
                    mmatrix.append(tmp1)
                matrix = mmatrix
            else:
                break
        return matrix[-1][-1]


pl = Pooling()
n = int(input().strip())
matrix = []
for i in range(n):
    line = list(map(int, input().strip().split(' ')))
    matrix.append(line)
res = pl.calc(n, matrix)
print(res)
