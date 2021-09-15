# 有向图打印所有的环
class Cycles:
    def findCycles(self, n, edges):
        def dfs(index,path):
            if visited[index] == 1 and path and index in path:
                res.append(path[path.index(index):])
                path = []
                return
            if sum(visited) == n:
                return
            path.append(index)
            visited[index] = 1
            for i in range(n):
                if edges[index][i] == 1:
                    dfs(i,path)
        visited = [0]*n
        res = []
        dfs(0,[])
        return res


c = Cycles()
edges = [[0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 0, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0]]
res = c.findCycles(len(edges), edges)
print(res)
