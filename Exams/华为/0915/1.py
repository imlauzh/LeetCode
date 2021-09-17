class LongestReSubString:
    def calc(self,str1):
        def func(length):
            seen=set()
            for i in range(n-length):
                if str1[i:i+length] not in seen:
                    seen.add(str1[i:i+length])
                else:
                    return str1[i:i+length]
            return None
        n=len(str1)
        left,right=1,n
        while left<right:
            mid=left+(right-left)//2
            if not func(mid):
                right=mid
            else:
                left=mid+1
        return left


lrss=LongestReSubString()
str1='ababab'
res=lrss.calc(str1)
print(str1[:res])
