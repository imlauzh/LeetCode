#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
# 按层模拟
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order


# 旋转矩阵
class Solution:
    def spiralOrder(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix[0]
            # 逆时针旋转90度
            matrix = list(zip(*matrix[1:]))[::-1]
        return res


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
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
# @lc code=end
