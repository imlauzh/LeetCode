# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def partition(l,r):
            p=l+(r-l)//2
            tinput[p],tinput[r]=tinput[r],tinput[p]
            i=l
            for j in range(l,r):
                if tinput[j]<tinput[r]:
                    tinput[j],tinput[i]=tinput[i],tinput[j]
                    i+=1
            tinput[i],tinput[r]=tinput[r],tinput[i]
            return i
        def qselect(l,r):
            if l>=r:
                return []
            mid=partition(l, r)
            if mid==k-1:
                return
            elif mid>k-1:
                qselect(l,mid)
            else:
                qselect(mid+1,r)
        qselect(0, len(tinput)-1)
        return tinput[:k]


# 暴力
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        list=[]
        if len(tinput)<k:
            return list
        else:
            tinput.sort()
            return tinput[:k]