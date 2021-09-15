#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
# 回溯法

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backTrack(index):
            if index == len(num):
                if len(seq) > 2:
                    res.append(seq[:])
                return
            curr = 0
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                curr = curr*10+ord(num[i])-ord('0')
                if curr > 2**31-1:
                    break
                if len(seq) < 2 or curr == seq[-2]+seq[-1]:
                    seq.append(curr)
                    backTrack(i+1)
                    seq.pop()
                elif len(seq) >= 2 and curr > seq[-1]+seq[-2]:
                    break
        res = []
        seq = []
        backTrack(0)
        return res[0] if res else seq
# @lc code=end
