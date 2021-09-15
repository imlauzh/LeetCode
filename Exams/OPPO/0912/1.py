class Solution:
    def spiral(self , n ):
        # write code here
        if n == 1:
            return [[1]]
        res = [[-1]*n for _ in range(n)]
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d, i, j = 0, 0, 0
        for idx in range(n**2):
            res[i][j] = n**2-idx
            ni, nj = i+direct[d][0], j+direct[d][1]
            if not (0 <= ni < n and 0 <= nj < n and res[ni][nj] == -1):
                d = (d+1) % 4
            i, j = i+direct[d][0], j+direct[d][1]
        return res


s = Solution()
n = int(input().strip())
res = s.spiral(n)
print(res)
