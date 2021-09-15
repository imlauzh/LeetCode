# 有名字列表和文章
# 统计所有名字出现的次数之和
# kmp只过了60
# 牛客上有分享说，按长度统计放到set中
# 然后按长度遍历，查看是否在set中，在的话+1
# 返回总长度


class Solution:
    def nameCount(self, nameList, page):
        def getNext(next, s):
            i, j = 0, -1
            next[0] = -1
            while i < len(s):
                if j == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]

        def kmp(s, t):
            res = 0
            m, n = len(s), len(t)
            next = [0]*(m+1)
            i, j = 0, 0
            getNext(next, s)
            while i < m and j < n:
                if i == -1 or s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    i = next[i]
                if i == m:
                    res += 1
                    i = next[i]
            return res
        ans = 0
        nameList = list(set(nameList))
        for name in nameList:
            if name in page:
                ans += kmp(name, page)
            # print(kmp(name, page))
        return ans


if __name__ == "__main__":
    import sys
    names = str(sys.stdin.readline().strip())
    names = names.split(' ')
    page = str(sys.stdin.readline().strip())
    s = Solution()
    ans = s.nameCount(names, page)
    print(ans)


# class Solution:
#     def nameCount(self, nameList, page):
#         def getNext(next, s):
#             i, j = 0, -1
#             next[0] = -1
#             while i < len(s):
#                 if j == -1 or s[i] == s[j]:
#                     i += 1
#                     j += 1
#                     next[i] = j
#                 else:
#                     j = next[j]

#         def kmp(s, t):
#             res = 0
#             m, n = len(s), len(t)
#             next = [0]*(m+1)
#             i, j = 0, 0
#             getNext(next, s)
#             while i < m and j < n:
#                 if i == -1 or s[i] == t[j]:
#                     i += 1
#                     j += 1
#                 else:
#                     i = next[i]
#                 if i == m:
#                     res += 1
#                     i = next[i]
#             return res
#         ans = 0
#         nameList = list(set(nameList))
#         nameList = sorted(nameList, reverse=True)
#         names = dict()
#         for name in nameList:
#             if name in names.keys():
#                 continue
#             flag = False
#             for key in names.keys():
#                 # print(key)
#                 if len(name) < len(key) and name in key:
#                     flag = True
#                     names[key] += 1
#             if not flag:
#                 names[name] = 1
#             # print(names)
#         for name in names.keys():
#             if name in page:
#                 ans += kmp(name, page)*names[name]
#             # print(kmp(name, page))
#         return ans


# if __name__ == "__main__":
#     import sys
#     names = str(sys.stdin.readline().strip())
#     names = names.split(' ')
#     page = str(sys.stdin.readline().strip())
#     s = Solution()
#     ans = s.nameCount(names, page)
#     print(ans)