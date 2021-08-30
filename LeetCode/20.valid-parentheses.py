#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=0
        while i<len(s):
            if s[i] in ['(','[','{']:
                stack.append(s[i])
                i+=1
            else:
                if not stack:
                    return False
                elif s[i]==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif s[i]==']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                if s[i]=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
                i+=1
        if stack:
            return False
        return True


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        maps={")": "(", "}": "{", "]": "["}
        stack=[]

        for char in s:
            if char in maps:
                if stack:
                    top=stack.pop()
                    if top!=maps[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return not stack
# @lc code=end

