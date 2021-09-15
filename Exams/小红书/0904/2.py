#!/bin/python
# -*- coding: utf8 -*-
# 分割段式回文，要求分割出来的子串是段式回文串
# 返回所有的分割方案
class Solution:
    def partitionNumber(self, s):
        # Write Code Here
        def BackTrack(pos):
            nonlocal res
            if pos == n:
                res += 1
                return
            for i in range(pos, n):
                if dp[pos][i] is True:
                    BackTrack(i+1)
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n):
            for j in range(i+1, n):
                left, right = i, j
                dp[i][j] = False
                while left < right:
                    if s[i:left+1] == s[right:j+1]:
                        dp[i][j] = True
                    left += 1
                    right -= 1
        res = 0
        BackTrack(0)
        return res


try:
    _text = input()
except:
    _text = None


s = Solution()
res = s.partitionNumber(_text)

print(str(res) + "\n")
