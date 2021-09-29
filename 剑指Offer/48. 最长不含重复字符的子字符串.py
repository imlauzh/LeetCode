class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        res, j = 0, -1
        for i in range(n):
            if i > 0:
                seen.remove(s[i-1])
            while j+1 < n and s[j+1] not in seen:
                j += 1
                seen.add(s[j])
            res = max(res, j-i+1)
        return res
