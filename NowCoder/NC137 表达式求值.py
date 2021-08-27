#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#
class Solution:
    def calc(self, nums, ops):
        if not nums or len(nums) < 2:
            return
        if not ops:
            return
        b, a, op = nums.pop(), nums.pop(), ops.pop()
        res = 0
        if op == '+':
            res = a+b
        elif op == '-':
            res = a-b
        elif op == '*':
            res = a*b
        nums.append(res)

    def solve(self, s):
        # write code here
        op_priority = {'+': 0, '-': 0, '*': 1}
        nums, ops = [0], ['+']
        n = len(s)

        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit():
                num = int(s[i])
                while i+1 < n and s[i+1].isdigit():
                    num = num*10+int(s[i+1])
                    i += 1
                nums.append(num)
            elif s[i] == '(':
                ops.append(s[i])
            elif s[i] == ')':
                while ops and ops[-1] != '(':
                    self.calc(nums, ops)
                ops.pop()
            else:
                while ops and ops[-1] != '(':
                    if op_priority[ops[-1]] < op_priority[s[i]]:
                        break
                    self.calc(nums, ops)
                ops.append(s[i])
            i += 1
        while ops:
            self.calc(nums, ops)
        return nums[0]
