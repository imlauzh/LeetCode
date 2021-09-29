class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        for i in range(26):
            L=0
            R=len(s)-1
            while L<len(s) and s[L]!=chr(i+97):L+=1
            while R>0 and s[R]!=chr(i+97):R-=1
            if L>=R:continue
            res=[0]*26
            for j in range(L+1,R):
                res[ord(s[j])-97]=1
            for x in res:ans+=x
        return ans