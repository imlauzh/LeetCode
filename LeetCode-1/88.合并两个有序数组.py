#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
# 1. 暴力
# 2. 从后往前遍历，注意边界情况

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m+n-1
        i, j = m-1, n-1
        while i>=0 and j>=0:
            if nums1[i]>= nums2[j]:
                # left greater
                nums1[pos] = nums1[i]
                i-=1
            else:
                nums1[pos] = nums2[j]
                j-=1
            pos-=1
        while j>=0:
            nums1[pos] = nums2[j]
            j-=1
            pos-=1
# @lc code=end

