#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
# 双指针
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        m, n = len(firstList), len(secondList)
        first, second = 0, 0
        res = []
        while first < m and second < n:
            fi, fj = firstList[first]
            si, sj = secondList[second]
            if max(fi, si) <= min(fj, sj):
                res.append([max(fi, si), min(fj, sj)])
            if fj <= sj:
                first += 1
            else:
                second += 1
        return res

        
# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        m, n = len(firstList), len(secondList)
        first, second = 0, 0
        res = []
        while first < m and second < n:
            fi, fj = firstList[first]
            si, sj = secondList[second]
            if max(fi, si) <= min(fj, sj):
                res.append([max(fi, si), min(fj, sj)])
            if fj <= sj:
                first += 1
            else:
                second += 1
        return res
# @lc code=end
