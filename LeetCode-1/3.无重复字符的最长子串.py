#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
# 每个字符开始的子串=》最长

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
# @lc code=end


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        l, r = 0, 0
        chars = defaultdict(int)
        while r<n:
            chars[s[r]]+=1
            while chars[s[r]]>1:
                chars[s[l]]-=1
                if chars[s[l]]==0:
                    del chars[s[l]]
                l+=1
            # print(l ,r, chars)
            ans = max(ans, len(chars))
            r+=1
        return ans
# @lc code=end