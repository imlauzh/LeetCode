#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
# 转换成数字做，不符合题目要求
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return 0
        m, n = len(num1), len(num2)
        n1, res = 0, 0
        for i in range(m):
            n1 = n1*10+ord(num1[i])-ord('0')
        for i in range(n):
            res += (ord(num2[i])-ord('0'))*(10**(n-1-i))*n1
        return str(res)


# 做加法
# 模拟「竖式乘法」
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            # 补0
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)

        return ans

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])


# 做乘法
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # 两个数字乘积的最大长度为m+n，可以证明
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        # 去除开始的0
        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # 两个数字乘积的最大长度为m+n，可以证明
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        # 去除开始的0
        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans
# @lc code=end
