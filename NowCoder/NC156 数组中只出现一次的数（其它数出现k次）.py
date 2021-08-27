#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int一维数组
# @param k int
# @return int
#
class Solution:
    def foundOnceNumber(self, arr, k):
        # write code here
        cnt = {}
        for i in arr:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        for i in cnt:
            if cnt[i] == 1:
                return i
