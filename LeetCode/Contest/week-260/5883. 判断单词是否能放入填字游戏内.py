class Solution:
    # 使用遍历的手段
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        nr, nc = len(board), len(board[0])
        wordLen = len(word)
        # 遍历行
        for i in range(nr):
            k = 0
            for j in range(nc+1):
                if j < nc and board[i][j] != '#':
                    continue
                if j - k != wordLen:  # 是否长度匹配
                    k = j + 1
                    continue
                # 正向检查
                if all(p1 == ' ' or p1 == p2 for p1, p2 in zip(board[i][k:j], word)):
                    return True
                if all(p1 == ' ' or p1 == p2 for p1, p2 in zip(board[i][k:j], word[::-1])):
                    return True
        # 遍历列
        for j in range(nc):
            k = 0
            for i in range(nr+1):
                if i < nr and board[i][j] != '#':
                    continue
                if i - k != wordLen:  # 是否长度匹配
                    k = i + 1
                    continue
                # 正向检查
                if all(p1 == ' ' or p1 == p2 for p1, p2 in zip((board[s][j] for s in range(k, i)), word)):
                    return True
                if all(p1 == ' ' or p1 == p2 for p1, p2 in zip((board[s][j] for s in range(k, i)), word[::-1])):
                    return True
        return False
