"""
2 3 10
S##
.#G

2 3 10
S##
..G
"""


class Maze:
    def calc(self, H, W, T, maze):
        def find(s):
            for i in range(H):
                for j in range(W):
                    if maze[i][j] == s:
                        maze[i-1][j]=' '
                        maze[i+1][j]=' '
                        maze[i][j-1]=' '
                        maze[i][j+1]=' '
                        return (i, j)
        si, sj = find('S')
        gi, gj = find('G')
        print(maze)
        dp = [[(0, 0)]*(abs(sj-gj)+1) for _ in range(abs(si-gi)+1)]
        dp[0][1],dp[1][0]=(0,1),(0,1)
        dp[-1][-2],dp[-2][-1]=(0,1),(0,1)
        di = 1 if si < gi else -1
        dj = 1 if sj < gj else -1
        print(dp,di,dj)
        for i in range(si,gi+1,di):
            for j in range(sj,gj+1,dj):
                if maze[i][j]=='.':
                    dp[i][j]=(dp[i][j][0],min(dp[i-1][j],dp[i+1][j],dp[i][j-1],dp[i][j+1])+1)
                elif maze[i][j]=='#':
                    dp[i][j]=(dp[i][j][0]+1,min(dp[i-1][j],dp[i+1][j],dp[i][j-1],dp[i][j+1])+1)

m = Maze()
H, W, T = list(map(int, input().strip().split(' ')))
maze = []
for i in range(H):
    w = list(input().strip())
    maze.append(w)
res = m.calc(H, W, T, maze)
print(res)
