# -*- coding:utf-8 -*-

class Solution:
    def findKth(self, a, n, k):
        # write code here
        def partition(l, r):
            p = l+(r-l)//2
            a[p], a[r] = a[r], a[p]
            i = l
            for j in range(l, r):
                if a[j] > a[r]:
                    a[j], a[i] = a[i], a[j]
                    i += 1
            a[i], a[r] = a[r], a[i]
            return i

        def qselect(l, r):
            if l >= r:
                return
            mid = partition(l, r)
            if mid == k-1:
                return
            elif mid > k-1:
                qselect(l, mid)
            else:
                qselect(mid+1, r)
        qselect(0, n-1)
        return a[k-1]
