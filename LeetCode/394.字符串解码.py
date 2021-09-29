#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                tmp = ''
                while stack[-1] != '[':
                    tmp += stack.pop()
                stack.pop()
                times = ''
                while stack and stack[-1].isdigit():
                    times = stack.pop()+times
                print(times)
                tmp = tmp*int(times)
                for i in range(len(tmp)-1, -1, -1):
                    stack.append(tmp[i])
        return ''.join(stack)
# @lc code=end
