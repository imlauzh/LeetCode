#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
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
        elif op == '/':
            res = a//b
        elif op == '^':
            res = pow(a, b)
        elif op == '%':
            res = a % b
        nums.append(int(res))

    def calculate(self, s: str) -> int:
        op_priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1, '^': 2}
        n = len(s)
        nums, ops = [0], ['+']

        i = 0
        while i < n:
            c = s[i]
            i += 1
            if c == ' ':
                continue
            if c.isdigit():
                # 处理数字
                num = int(c)
                while i < n and s[i].isdigit():
                    num = num*10+int(s[i])
                    i += 1
                nums.append(num)
            elif c == '(':
                ops.append(c)
            elif c == ')':
                # 遇到右括号就把括号里面的计算完
                while ops:
                    if ops[-1] != '(':
                        self.calc(nums, ops)
                    else:
                        ops.pop()
                        break
            else:
                # 其他操作符，根据优先级计算
                # 把栈内优先级高于或等于该操作的先计算
                # 例如ops=[*]，nums=[1,2]
                # 当前操作为+，先计算乘法
                while ops and ops[-1] != '(':
                    prev_op = ops[-1]
                    if op_priority[prev_op] < op_priority[c]:
                        break
                    self.calc(nums, ops)
                ops.append(c)
        while ops:
            self.calc(nums, ops)
        return nums[0]
# @lc code=end
