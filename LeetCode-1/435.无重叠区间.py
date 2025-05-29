#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        # print(intervals)
        ans = 0
        cur_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]>=cur_end:
                cur_end = intervals[i][1]
            else:
                ans += 1
        return ans
# @lc code=end


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[1]) # 按结束时间排序
        
        kept_count = 1 # 第一个区间总是被保留
        cur_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= cur_end: # 如果当前区间不与上一个保留的区间重叠
                kept_count += 1          # 保留当前区间
                cur_end = intervals[i][1] # 更新保留区间的结束时间
            # else: 当前区间与已保留的区间重叠，由于我们优先保留结束早的，所以这个重叠的就被忽略（相当于移除）
                
        return len(intervals) - kept_count # 总数 - 最多保留数 = 最少移除数
# @lc code=end