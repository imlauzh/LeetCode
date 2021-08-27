#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算模板串S在文本串T中出现了多少次
# @param S string字符串 模板串
# @param T string字符串 文本串
# @return int整型
#
class Solution:
    def getNext(self, next, s):
        j, k = 0, -1
        next[0] = -1
        while j < len(s):
            if k == -1 or s[j] == s[k]:
                j += 1
                k += 1
                next[j] = k
            else:
                k = next[k]

    def kmp(self, S, T):
        res = 0
        m, n = len(S), len(T)
        next = [0]*(m+1)
        i, j = 0, 0
        self.getNext(next, S)
        while i < m and j < n:
            if i == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                i = next[i]
            if i == m:
                res += 1
                i = next[i]
        return res
