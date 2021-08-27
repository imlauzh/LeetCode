#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        left, right = 0, n-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrome(left+1, right) or checkPalindrome(left, right-1)
        return True
# @lc code=end
