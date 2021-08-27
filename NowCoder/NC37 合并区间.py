# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i: i.start)

        result = []
        for i in intervals:
            if not result or result[-1].end < i.start:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)
        return result
