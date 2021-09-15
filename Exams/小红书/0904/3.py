# 路径和小于最大值k记为朋友，返回朋友对的个数
# 深度优先搜索，注意去重
class Friends:
    def calNum(self, n, k, edges):
        def dfs(start, index, target):
            # if start!=index and target >= 0:
            #     res.add((start, index))
            if target >= 0:
                if start < index:
                    res.add((start, index))
                elif start > index:
                    res.add((index, start))
            for i in range(n):
                if target-maps[index][i] >= 0:
                    dfs(start, i, target-maps[index][i])

        maps = [[float('inf')]*n for _ in range(n)]
        for i in range(n-1):
            maps[edges[3*i]-1][edges[3*i+1]-1] = edges[3*i+2]
            maps[edges[3*i+1]-1][edges[3*i]-1] = edges[3*i+2]
        res = set()
        for i in range(n):
            dfs(i, i, k)
        return res


friend = Friends()
nums = input().strip()
nums = list(map(int, nums.split(' ')))
n, k = nums[0], nums[1]
edges = input().strip()
edges = list(map(int, edges.split(' ')))
res = friend.calNum(n, k, edges)
print(res)
print(len(res))
