#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
# @lc code=end


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        l,r = 0, len(sgood)-1
        while l<r:
            if sgood[l]!=sgood[r]:
                return False
            l+=1
            r-=1
        return True
# @lc code=end

