#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i = j = di = 0
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4
            i += DIRS[di][0]
            j += DIRS[di][1]
        return ans
# @lc code=end

