#
# @lc app=leetcode.cn id=2105 lang=python3
#
# [2105] 给植物浇水 II
#

# @lc code=start
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        l, r = 0, len(plants) - 1
        ca, cb = capacityA, capacityB
        while l < r:
            # print(plants[l], ca, plants[r], cb)
            if ca >= plants[l]:
                ca -= plants[l]
            else:
                ans += 1
                ca = capacityA - plants[l]
            if cb >= plants[r]:
                cb -= plants[r]
            else:
                ans += 1
                cb = capacityB - plants[r]
            l += 1
            r -= 1
        if l == r and not (ca >= plants[l] or cb >= plants[l]):
            ans += 1
        return ans

# @lc code=end

