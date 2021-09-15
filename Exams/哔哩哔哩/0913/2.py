"""
弹幕蒙版
时间限制： 3000MS
内存限制： 589824KB
题目描述：
在B站观看视频过程中，当画面中弹幕比较多的时候，会发现主要物体不会被弹幕遮挡，这就是智能防挡的功能。现在假设画面中有多个主要物体不会被遮挡，每个物体是由相邻的1（代表物体内部点）构成的连通区域，这里的相邻要求两个 1 必须在水平或者竖直方向上相邻，非物体区域用0表示。



输入描述
现在可以用一个由[0,1]组成的二维数组表示整张图的弹幕蒙版

输出描述
返回其中最大的物体的面积大小。



样例输入
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,1,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
样例输出
10

提示
输入格式请严格参照“输入样例”中给出的格式

蒙版的数组范围均在100000以内
"""


class Tanmu:
    def calc(self, matrix):
        def dfs(i, j):
            res = 0
            res += matrix[i][j]
            visited[i][j] = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < nr and 0 <= y < nc and matrix[x][y] == 1 and visited[x][y] == 0:
                    res += dfs(x, y)
            return res
        nr, nc = len(matrix), len(matrix[0])
        visited = [[0]*nc for _ in range(nr)]
        res = 0
        for i in range(nr):
            for j in range(nc):
                if visited[i][j] == 0 and matrix[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res


tm = Tanmu()
matrix = []
while True:
    try:
        line = list(map(int, input().strip(' ').strip(
            '[').strip(',').strip(']').split(',')))
        if line == '':
            break
        matrix.append(line)
    except:
        break
res=tm.calc(matrix)
print(res)