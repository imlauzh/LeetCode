#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 注意除法为int(x/y)
        # Python 直接用 // 遇到负数会出现问题，需要用 int(a / b)
        op_priority_func = {'+': add, '-': sub,
                            '*': mul, '/': lambda x, y: int(x/y)}
        stack = list()
        for token in tokens:
            # 这里不好使用isdigit判断
            # 因为并不是单个数字,且包含符号
            if token not in ["+", "-", "*", "/"]:
                num = int(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_priority_func[token](num1, num2)
            stack.append(num)
        return stack[0]
# @lc code=end
