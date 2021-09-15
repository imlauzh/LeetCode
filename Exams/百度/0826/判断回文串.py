# 判断字符串是否为回文串
# 字符串可以包含数字大小写字母，忽略其他字符


class Solution:
    def Palindrome(self,s:str):
        i,j=0,len(s)-1
        while i<j:
            while i<j and not ('0'<=s[i]<='9' or 'a'<=s[i]<='z' or 'A'<=s[i]<='Z'):
                i+=1
            while i<j and not ('0'<=s[j]<='9' or 'a'<=s[j]<='z' or 'A'<=s[j]<='Z'):
                j-=1
            if i>=j:
                break
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True

if __name__ == "__main__":
    strs=['a^&*bc*)(ba1','*)','Abd@1#s!@1D*^)(ba']
    s=Solution()
    for i in strs:
        print(s.Palindrome(i))
