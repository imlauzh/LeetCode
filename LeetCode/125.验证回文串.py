#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
# 只考虑字母和数字
# 双指针跳过不符合的字符
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(c):
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                return True
            return False
        if len(s) < 1:
            return True
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not check(s[left]):
                left += 1
            while left < right and not check(s[right]):
                right -= 1
            if left >= right:
                break
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(c):
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                return True
            return False
        if len(s) < 1:
            return True
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not check(s[left]):
                left += 1
            while left < right and not check(s[right]):
                right -= 1
            if left >= right:
                break
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
# @lc code=end
