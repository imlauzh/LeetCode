#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False
# @lc code=end

