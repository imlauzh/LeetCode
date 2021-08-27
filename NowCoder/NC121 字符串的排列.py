# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, s):
        # write code here
        def nextPermutation(s):
            i = len(s)-2
            while i >= 0 and s[i] >= s[i+1]:
                i -= 1
            if i < 0:
                return False
            j = len(s)-1
            while j >= 0 and s[j] <= s[i]:
                j -= 1
            s[i], s[j] = s[j], s[i]
            left, right = i+1, len(s)-1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return True
        if len(s) < 2:
            return [s]
        s = sorted(list(s))
        res = []
        res.append(''.join(s))
        while True:
            if not nextPermutation(s):
                break
            res.append(''.join(s))
        return res
