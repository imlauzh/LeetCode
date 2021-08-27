# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, arr):
        # write code here
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] < arr[r]:
                return arr[l]
            mid = (l+r)//2
            # 注意这里不能和左端点进行比较
            # 情况1 ：1 2 3 4 5 ， arr[mid] = 3. target = 1, arr[mid] > target, 答案在mid 的左侧
            # 情况2 ：3 4 5 1 2 ， arr[mid] = 5, target = 3, arr[mid] > target, 答案却在mid 的右侧
            # 所以不能把左端点当做target
            if arr[mid] == arr[r]:
                r -= 1
            elif arr[mid] < arr[r]:
                r = mid
            else:
                l = mid+1
        return arr[l]
