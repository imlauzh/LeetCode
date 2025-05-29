#
# @lc app=leetcode.cn id=1471 lang=python3
#
# [1471] 数组中的 k 个最强值
#

# @lc code=start
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        ans = []
        l, r = 0, n - 1
        while len(ans) < k:
            if abs(arr[l] - m) > abs(arr[r] - m):
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1
        return ans

# @lc code=end

