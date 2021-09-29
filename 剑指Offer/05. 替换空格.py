class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)
