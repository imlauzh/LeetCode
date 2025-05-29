#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                vowel+=1
            if i < k-1:
                continue
            ans = max(ans, vowel)
            if s[i-k+1] in 'aeiou':
                vowel-=1
        return ans
# @lc code=end
