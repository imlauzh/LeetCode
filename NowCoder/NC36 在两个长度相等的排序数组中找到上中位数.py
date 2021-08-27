#
# find median in two sorted array
# @param arr1 int整型一维数组 the array1
# @param arr2 int整型一维数组 the array2
# @return int整型
#
class Solution:
    def findMedianinTwoSortedAray(self, arr1, arr2):
        # write code here
        n = len(arr1)
        target = n
        l, r = 0, 0
        while target > 0 and (l < n or r < n):
            if l < n and arr1[l] <= arr2[r]:
                res = arr1[l]
                l += 1
                target -= 1
            elif r < n:
                res = arr2[r]
                r += 1
                target -= 1
        return res
