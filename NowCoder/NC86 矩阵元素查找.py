# -*- coding:utf-8 -*-

class Solution:
    def findElement(self, mat, n, m, x):
        # write code here
        i, j = 0, m-1
        while i < n and j >= 0:
            if mat[i][j] == x:
                return [i, j]
            elif mat[i][j] < x:
                i += 1
            else:
                j -= 1
        return []
