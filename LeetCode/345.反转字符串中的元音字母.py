#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
# 双指针，从两头开始遍历
# 遇到两个都是元音，替换
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s)-1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            if left >= right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s)-1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            if left >= right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
# @lc code=end
