#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
# 先找行，再找列
# 不过还可以再优化：去除辅助行，二分找行
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row):
            left, right = 0, nc-1
            while left <= right:
                mid = left+(right-left)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return False
        nr, nc = len(matrix), len(matrix[0])
        matrix.append([float('inf')]*nc)
        i = 0
        while i < nr:
            if matrix[i][0] <= target < matrix[i+1][0]:
                return binarySearch(i)
            i += 1
        return False


# 把二维数组拼成一维，用二分
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr, nc = len(matrix), len(matrix[0])
        left, right = 0, nr*nc-1
        while left <= right:
            mid = left+(right-left)//2
            i, j = mid//nc, mid % nc
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid-1
            else:
                left = mid+1
        return False


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 更加规范的二分法
        row, col = len(matrix), len(matrix[0])
        # 记录找到的位置
        x, y = 0, 0
        # 查找列
        high, low = 0, row-1
        while high <= low:
            mid = (high + low) // 2
            if target <= matrix[mid][col-1]:
                x = mid
                low = mid - 1
            else:
                high = mid + 1

        # 查找行
        left, right = 0, col-1
        while left <= right:
            mid = (left + right) // 2
            if target <= matrix[x][mid]:
                y = mid
                right = mid - 1
            else:
                left = mid + 1

        return matrix[x][y] == target
# @lc code=end
