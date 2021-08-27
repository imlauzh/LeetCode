#
#
# @param strs string字符串一维数组
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self, strs):
        # write code here
        if not strs:
            return ""
        res = ""
        minLen = min([len(i) for i in strs])
        for i in range(minLen):
            curr = strs[0][i]
            # all(): 判断给定的可迭代参数iterable 中的所有元素是否都为TRUE
            if all(s[i] == curr for s in strs):
                res += curr
            else:
                return res
        return res
