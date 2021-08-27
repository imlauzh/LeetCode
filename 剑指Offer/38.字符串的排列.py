#
# @lc app=leetcode.cn id=2044 lang=python3
#
# [2044] 剑指 Offer 38. 字符串的排列
# 先排序，保证开始是最小的
# 然后加入下一个比他大的排列
# 这里用两次遍历，从后往前
# 当前某一部分肯定是递减的序列，也就是最大的，那么下一个
# 也就是这部分从最大变成最小，然后前一个字符变大一个即可
# 例如123 6 87543-->123 7 34568


# @lc code=start
class Solution:
    def permutation(self, s: str) -> List[str]:
        def nextPermutation(s):
            i = len(s)-2
            while i >= 0 and s[i] >= s[i+1]:
                i -= 1
            if i < 0:
                return False
            j = len(s)-1
            while j >= 0 and s[j] <= s[i]:
                j -= 1
            s[i], s[j] = s[j], s[i]
            left, right = i+1, len(s)-1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return True

        if len(s) < 2:
            return [s]
        s = sorted(list(s))
        res = [''.join(s)]
        while True:
            if not nextPermutation(s):
                break
            res.append(''.join(s))
        return res

# @lc code=end
