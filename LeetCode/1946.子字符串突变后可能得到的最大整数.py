#
# @lc app=leetcode.cn id=1946 lang=python3
#
# [1946] 子字符串突变后可能得到的最大整数
#

# @lc code=start
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num=list(num)
        n = len(num)
        flag=False
        for i in range(n):
            curr = int(num[i])
            nxt = change[curr]
            if nxt > curr:
                num[i]=str(nxt)
                flag=True
            elif nxt < curr:
                if flag:break
        return ''.join(num)
# @lc code=end
