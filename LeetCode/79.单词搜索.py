#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isSubExist(i, j, k):
            # 当前字母不匹配
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True

            visited.add((i, j))
            res = False
            for ix, jy in directions:
                ni, nj = i+ix, j+jy
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if (ni, nj) not in visited:
                        # 未被访问过判断下一长度匹配
                        if isSubExist(ni, nj, k+1):
                            res = True
                            break
            # 回溯，恢复状态
            visited.remove((i,j))
            return res

        m, n = len(board), len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if isSubExist(i, j, 0):
                    return True
        return False

# @lc code=end
