n, m = [int(i) for i in input().strip().split()]
g = [[1 if c == 'r' else 0 for c in input().strip()] for i in range(n)]
x, y = [int(i) for i in input().strip().split()]


cnt = 0
def func(i, j, c):
    if i < 0 or j < 0 or i >= len(g) or j >= len(g[0]) or g[i][j] == -1 or g[i][j] != c:
        return
    cnt += 1
    g[i][j] = -1
    nc = c ^ 1
    func(i-2, j-1, nc)
    func(i-2, j+1, nc)
    func(i-1, j+2, nc)
    func(i+1, j+2, nc)
    func(i+2, j+1, nc)
    func(i+2, j-1, nc)
    func(i+1, j-2, nc)
    func(i-1, j+2, nc)
    
func(x-1, y-1, g[x-1][y-1])
print(cnt)


# s = prob3()
# res = s.calc(g, x, y)
# print(res)
