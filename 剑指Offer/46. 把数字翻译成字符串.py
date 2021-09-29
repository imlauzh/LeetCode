class Solution:
    def translateNum(self, num: int) -> int:
        def backTrack(index):
            nonlocal res
            if index == len(num):
                res += 1
                return
            if num[index] == '0':
                backTrack(index+1)
                return
            tmp = 0
            for i in range(index, len(num)):
                tmp = tmp*10+ord(num[i])-ord('0')
                if tmp < 26:
                    backTrack(i+1)
                else:
                    break
        res = 0
        num = str(num)
        backTrack(0)
        return res
