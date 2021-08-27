#
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def spiralOrder(self , matrix ):
        # write code here
        if not matrix or not matrix[0]:
            return list()
        m, n = len(matrix), len(matrix[0])
        visited = [[0]*n for _ in range(m)]
        ds = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [0]*(m*n)
        i, j, d = 0, 0, 0
        for idx in range(m*n):
            res[idx] = matrix[i][j]
            visited[i][j] = 1
            tmp_i, tmp_j = i+ds[d][0], j+ds[d][1]
            if not(0 <= tmp_i < m and 0 <= tmp_j < n) or visited[tmp_i][tmp_j] == 1:
                d = (d+1) % 4
            i += ds[d][0]
            j += ds[d][1]
        return res