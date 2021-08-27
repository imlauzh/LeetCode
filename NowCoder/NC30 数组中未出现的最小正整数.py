#
# return the min number
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def minNumberdisappered(self, arr):
        # write code here
        x = 1
        while x in arr:
            x += 1
        return x
