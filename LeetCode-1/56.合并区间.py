#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        n = len(intervals)
        l, r = 0, 0
        max_right = intervals[l][1]
        for r in range(1, n):
            if intervals[r][0] <= max_right:
                max_right = max(max_right, intervals[r][1])
            else:
                ans.append([intervals[l][0], max_right])
                max_right = intervals[r][1]
                l = r
        ans.append([intervals[l][0], max_right])
        return ans

# @lc code=end


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 可以合并
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
            else:  # 不相交，无法合并
                ans.append(p)  # 新的合并区间
        return ans
