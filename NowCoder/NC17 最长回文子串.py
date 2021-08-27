# -*- coding:utf-8 -*-

class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        def helper(l, r):
            while 0 <= l < len(A) and 0 <= r < len(A) and A[l] == A[r]:
                l -= 1
                r += 1
            return A[l+1:r]

        if not A:
            return 0
        res = -1
        for i in range(len(A)):
            a = helper(i, i)
            b = helper(i, i+1)
            res = max(res, len(a))
            res = max(res, len(b))
        return res
