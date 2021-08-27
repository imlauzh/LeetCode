#
# 反转字符串
# @param str string字符串 
# @return string字符串
#
class Solution:
    def solve(self , str ):
        # write code here
        return str[::-1]


#
class Solution:
    def solve(self , str ):
        # write code here
        res=""
        for i in range(len(str)-1,-1,-1):
            res+=str[i]
        return res