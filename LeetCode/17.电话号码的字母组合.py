#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# 回溯法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        combine = []

        def backTrack(pos):
            if pos == len(digits):
                res.append(''.join(combine))
                return
            digit = digits[pos]
            for letter in phoneMap[digit]:
                combine.append(letter)
                backTrack(pos+1)
                combine.pop()
        backTrack(0)
        return res


# @lc code=start
# 队列法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        queue = ['']
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phoneMap[digit]:
                    queue.append(tmp+letter)
        return queue
# @lc code=end
