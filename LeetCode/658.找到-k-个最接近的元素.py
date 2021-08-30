#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<=arr[0]:
            return arr[:k]
        elif x>=arr[-1]:
            return arr[-k:]
        n = len(arr)
        left, right = 0, n-k-1
        while left <= right:
            mid = left+(right-left)//2
            # 排好序的数组，那么就是窗口为k的子数组
            # 找到窗口的头的距离接近尾的距离
            if x-arr[mid] > arr[mid+k]-x:
                left = mid+1
            else:
                right = mid-1
        return arr[left:left+k]
# @lc code=end
