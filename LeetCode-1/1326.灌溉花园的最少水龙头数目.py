#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#

# @lc code=start
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        explode_ranges = []
        for i in range(n+1):
            explode_ranges.append([max(0, i-ranges[i]), i+ranges[i]])
        explode_ranges.sort(key=lambda x:(x[0], -x[1]))
        print(explode_ranges)
        cur_e, next_e = 0, 0
        ans = 0
        for i in range(n+1):
            if explode_ranges[i][0] == explode_ranges[i][1]:
                continue
            if explode_ranges[i][0]<=cur_e:
                next_e = max(next_e, explode_ranges[i][1])
            elif cur_e < explode_ranges[i][0] <= next_e:
                ans += 1
                cur_e = next_e
                next_e = max(next_e, explode_ranges[i][1])
                if cur_e >= n:
                    return ans
            else: return -1
            if next_e>=n:
                return ans+1
        return -1
                
# @lc code=end

