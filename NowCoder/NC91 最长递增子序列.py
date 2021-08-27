#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#
import bisect


class Solution:
    def LIS(self, arr):
        # write code here
        n = len(arr)
        d = []
        dp = [1]*n
        for i in range(n):
            j = bisect.bisect_left(d, arr[i])
            if j == len(d):
                d.append(arr[i])
            else:
                d[j] = arr[i]
            dp[i] = j+1
        l = len(d)
        res = [0]*l
        for i in range(n-1, -1, -1):
            if dp[i] == l:
                res[l-1] = arr[i]
                l -= 1
        return res
