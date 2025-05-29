#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = cur_num = 0
        bucks = defaultdict(int)
        l, r = 0, 0
        n = len(fruits)
        while r < n:
            bucks[fruits[r]] += 1
            cur_num += 1
            while len(bucks) > 2 and l < r:
                bucks[fruits[l]] -= 1
                if bucks[fruits[l]] == 0:
                    del bucks[fruits[l]]
                l += 1
                cur_num -= 1
            if len(bucks) <= 2:
                ans = max(ans, cur_num)
            r += 1
        return ans

# @lc code=end

