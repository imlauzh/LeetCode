#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        maps={")": "(", "}": "{", "]": "["}
        stack=[]
        for c in s:
            if c not in maps:
                stack.append(c)
            else:
                if stack:
                    top=stack.pop()
                    if top!=maps[c]:
                        return False
                else:
                    return False
        return not stack
# @lc code=end

