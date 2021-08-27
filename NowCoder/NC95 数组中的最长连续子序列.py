#
# max increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def MLS(self, arr):
        # write code here
        arr = set(arr)
        res = 1
        for i in arr:
            if i-1 not in arr:
                curr = i
                tmp = 1
                while curr+1 in arr:
                    curr += 1
                    tmp += 1
                res = max(res, tmp)
        return res
