#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
# 双指针
class Solution:
    def LCS(self, str1, str2):
        # write code here
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        res = ''
        maxLen = 0
        for i in range(len(str1)):
            # 如果加一个字符也存在str2中的话,就更新res以及指针位置
            if str1[i-maxLen:i+1] in str2:
                res = str1[i-maxLen:i+1]
                maxLen += 1
        return res
