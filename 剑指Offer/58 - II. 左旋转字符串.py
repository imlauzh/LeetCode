class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        for i in range(n):
            s.append(s.pop(0))
        return ''.join(s)


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        for i in range(n):
            s = s+s[i]
        return s[n:]
