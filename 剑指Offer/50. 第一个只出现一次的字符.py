class Solution:
    def firstUniqChar(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ' '
        seen = dict()
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for c in s:
            if seen[c] == 1:
                return c
        return ' '


# 第二遍遍历的时候不遍历字符串
# 遍历hash，看当前字符的val是否为-1
# -1说明该字符出现多次，
# python3.6以后的字典是插入有序的
# 所以可以保证返回的字符是第一个出现的不重复的字符
class Solution:
    def firstUniqChar(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ' '
        seen = dict()
        for i in range(n):
            if s[i] in seen:
                seen[s[i]] = -1
            else:
                seen[s[i]] = i
        for key, val in seen.items():
            if val != -1:
                return key
        return ' '


# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-by-3zqv5/
class Solution:
    def firstUniqChar(self, s: str) -> str:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((s[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return ' ' if not q else q[0][0]
