#
#
# @param str string字符串
# @return int整型
# 实现函数 atoi 。函数的功能为将字符串转化为整数
# 提示：仔细思考所有可能的输入情况。这个问题没有给出输入的限制，你需要自己考虑所有可能的情况。
#
class Solution:
    def atoi(self, str):
        # write code here
        str = str.strip()  # 删除首尾空格
        if not str:
            return 0  # 字符串为空则直接返回

        res, i, sign = 0, 1, 1
        int_max, int_min, boundary = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if str[0] == '-':
            sign = -1  # 保存负号
        elif str[0] != '+':
            i = 0  # 若无符号位，则需从 i = 0 开始数字拼接
        for c in str[i:]:
            if not '0' <= c <= '9':
                break  # 遇到非数字的字符则跳出
            if res > boundary or res == boundary and c > '7':
                return int_max if sign == 1 else int_min  # 数字越界处理
            res = 10 * res + ord(c) - ord('0')  # 数字拼接
        return sign * res
