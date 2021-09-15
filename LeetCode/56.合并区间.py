#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        i, res = 0, []
        while i < n:
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            elif res and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        i, res = 0, []
        while i < n:
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            elif res and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res
# @lc code=end
