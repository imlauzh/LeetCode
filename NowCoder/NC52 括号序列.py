#
# 
# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def isValid(self , s ):
        # write code here
        map={")":"(", "]":"[", "}":"{"}
        stack=[]
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack or stack[-1]!=map[c]:
                    return False
                stack.pop()
        return not len(stack)

class Solution:
    def isValid(self , s ):
        # write code here
        if len(s)%2!=0:
            return False
        if '[]' in s or '{}' in s or '()' in s:
            s=s.replace('()','').replace('{}','').replace('[]','')
        return s==''