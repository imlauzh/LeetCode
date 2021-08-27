#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
# 因为只有+和-操作以及括号，所以可以把减号转化成+号，记录当前的正负号
# 遇到左括号就把括号前的正负号加入栈中，遇到右括号再出栈
# 每个数字前的正负号是由前面的操作符和栈顶的符号一起决定的

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
        nums.append(res)

    def calculate(self, s: str) -> int:
        op_priority = {'+': 0, '-': 0}
        n = len(s)
        nums, ops = [0], ['+']

        i = 0
        while i < n:
            curr = s[i]
            i += 1
            if curr == ' ':
                continue
            elif curr.isdigit():
                num = int(curr)
                while i < n and s[i].isdigit():
                    num = num*10+int(s[i+1])
                    i += 1
                nums.append(num)
            elif curr == '(':
                ops.append(curr)
            elif curr == ')':
                while ops:
                    if ops[-1] != '(':
                        self.calc(nums, ops)
                    else:
                        ops.pop()
                        break
            else:
                while ops and ops[-1] != '(':
                    if op_priority[ops[-1]] < op_priority[curr]:
                        break
                    self.calc(nums, ops)
                ops.append(curr)
            print(nums, ops)
        while ops:
            self.calc(nums, ops)
        return nums[0]
# @lc code=end
