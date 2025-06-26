#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nlgn: 排序
        # n：遍历一遍，空间换时间
        # 数组的头尾相邻，如果不相邻，那么就新加一个数组, 但是查询的时间复杂度太高
        # hash表的查询复杂度是o1，改造
        # https://leetcode.cn/problems/longest-consecutive-sequence/solutions/3005726/ha-xi-biao-on-zuo-fa-pythonjavacgojsrust-whop
        ans = 0
        st = set(nums)
        for x in st:
            if x - 1 in st:
                continue
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y - x)
        return ans

# @lc code=end

