#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<arr[0]:
            return arr[:k]
        if x>arr[-1]:
            return arr[-k:]
        n = len(arr)
        ans = [0]*k
        # 要最接近的k个数，反过来做更直接：最远的n-k个数，剩下的就是答案
        l, r = 0, n-1
        while r-l+1>k:
            if abs(arr[l]-x)>abs(arr[r]-x):
                l+=1
            else:
                r-=1
        return arr[l:r+1]
# @lc code=end

