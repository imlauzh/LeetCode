#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param str string字符串 待判断的字符串
# @return bool布尔型
#
class Solution:
    def judge(self , str ):
        # write code here
        l,r=0,len(str)-1
        while l<r and str[l]==str[r]:
            l+=1
            r-=1
        if l>=r:
            return True
        return False