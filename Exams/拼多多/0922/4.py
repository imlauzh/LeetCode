"""
2
3 4 3 3
1 2 3
1 1
2 2
2 1
2 2
0 1 1 1
1 1
"""
class StoneMove:
    def calc(self, n, m, moves, x, y, start):
        operation = ['#', (-1, 0), (0, -1), (1, 0), (0, 1)]

        def move(start, op):
            if op >= n:
                return start
            i, j = start
            ni, nj = i+operation[moves[op]][0], j+operation[moves[op]][1]
            # print(moves[op],start,ni,nj)
            if 1 <= ni <= x and 1 <= nj <= y:
                # print(1)
                return move((ni, nj), op+1)
            else:
                # print(2)
                return move(start, op+1)
        res = move(start, 0)
        print(res[0], res[1])
    def calc1(self, n, m, moves, x, y, locs):
        def func(i, j, op):
            ni, nj = i+op[0], j+op[1]
            if 1 <= ni <= x and 1 <= nj <= y:
                return [ni,nj]
            else:
                return [i,j]
        operation = ['#', (-1, 0), (0, -1), (1, 0), (0, 1)]
        for move in moves:
            op = operation[move]
            for i in range(m):
                loc=locs[i]
                locs[i]=func(loc[0],loc[1],op)
        for i in range(m):
            print(locs[i][0],locs[i][1])
    def calc2(self, n, m, moves, x, y, locs):
        def func(i, j, op):
            ni, nj = i+op[0], j+op[1]
            return ni,nj
        operation = ['#', (-1, 0), (0, -1), (1, 0), (0, 1)]
        i,j=0,0
        for move in moves:
            op = operation[move]
            i,j=i+op[0], j+op[1]
        print(i,j)
        si,sj=func(1,1,(i,j))
        ei,ej=si+(x-1),sj+(y-1)
        print(si,sj,ei,ej)
        for i in range(m):
            print(locs[i])
            if not si<=locs[i][0]<=ei:
                locs[i][0]=si if locs[i][0]<si else ei
            if not sj<=locs[i][1]<=ej:
                locs[i][1]=sj if locs[i][1]<sj else ej
            print(locs[i])
        for i in range(m):
            print(locs[i][0],locs[i][1])


sm = StoneMove()
T = int(input().strip())
for t in range(T):
    n, m, x, y = list(map(int, input().strip().split(' ')))
    if n > 0:
        moves = list(map(int, input().strip().split(' ')))
        locs = []
        for _ in range(m):
            i, j = list(map(int, input().strip().split(' ')))
            locs.append([i, j])
        sm.calc2(n, m, moves, x, y, locs)
    else:
        for _ in range(m):
            i, j = list(map(int, input().strip().split(' ')))
            print(i, j)
