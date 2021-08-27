#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            # 计算到n行，计算答案
            if row == n:
                board = generateBoard()
                res.append(board)
            else:
                for i in range(n):
                    # 列，对角线，斜对角线
                    # 对角线上 行坐标-列下标用来区分
                    # 斜对角线上 行+列来区分
                    # i为列坐标
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                    
        res = list()
        # 每行queen位置
        queens = [-1] * n
        row = ["."] * n

        columns = set()
        diagonal1 = set()
        diagonal2 = set()

        backtrack(0)
        return res
# @lc code=end

