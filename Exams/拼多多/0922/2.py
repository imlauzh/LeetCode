"""
3
3 3 7
1 1 2
5 5 8
3 9 7
3 3 6
10 9 6
10 10 10
1 7 4
3 3 7
1 4 9
10 6 10
3 3 5

1
0
4
"""


class MatrixMove:
    def calc(self, n, m, k, matrix):
        def func(matrix, i, j, path):
            if not (0 <= i < n) or not (0 <= j < m) or matrix[i][j] in path:
                return 0
            elif i == n-1 and j == m-1:
                return 1
            else:
                path.append(matrix[i][j])
                res = func(matrix, i+1, j, path) + func(matrix, i, j+1, path)
                path.pop()
                return res
        res = func(matrix, 0, 0, [])
        print(res)


mm = MatrixMove()
T = int(input().strip())
for t in range(T):
    n, m, k = list(map(int, input().strip().split(' ')))
    matrix = []
    for _ in range(n):
        line = list(map(int, input().strip().split(' ')))
        matrix.append(line)
    mm.calc(n, m, k, matrix)
