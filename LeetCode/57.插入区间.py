#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
# 由于原始的区间列表是无重叠的，按照开始端点升序的
# 所以一次遍历分情况讨论即可
# 如果元素的左端点比right大，直接加入res
# 右端点比left小，直接加入
# 这两种情况是与新区间没有重叠，可以直接加入res
# 剩下的情况就是有重叠
# 可以通过扩展新区间的左右端点就可以
# 最后如果没有加入新区间，可以加入res
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        left, right = newInterval
        placed = False
        for ileft, iright in intervals:
            if ileft > right:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append([ileft, iright])
            elif iright < left:
                res.append([ileft, iright])
            else:
                left = min(left, ileft)
                right = max(right, iright)
        if not placed:
            res.append([left, right])
        return res
        

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        left, right = newInterval
        placed = False
        for ileft, iright in intervals:
            if ileft > right:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append([ileft, iright])
            elif iright < left:
                res.append([ileft, iright])
            else:
                left = min(left, ileft)
                right = max(right, iright)
        if not placed:
            res.append([left, right])
        return res
# @lc code=end
