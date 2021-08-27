#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
# 
class Solution:
    def maxsumofSubarray(self, arr):
        # write code here
        res, tmp = 0, 0
        for i in arr:
            # 累积和
            tmp += i
            # 如果当前小于0,说明这个值不要, 从下一个数字在开始
            if tmp < 0:
                tmp = 0
            # 每次都更新最大值
            res = max(res, tmp)
        return res
