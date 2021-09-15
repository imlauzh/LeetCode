class Solution:
    def longest_substr(self , s ):
        # write code here
        seen=set()
        res,n,j="",len(s),-1
        for i in range(n):
            if i!=0:
                seen.remove(s[i-1])
            while j+1<n and s[j+1] not in seen:
                j+=1
                seen.add(s[j])
            if j-i+1>len(res):
                res=s[i:j+1]
        return res

solu = Solution()
s = input().strip()
res = solu.longest_substr(s)
print(res)