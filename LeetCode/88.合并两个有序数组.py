#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
# 从后面开始判断效率更高，哪个大先放进去

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m+n-1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
            else:
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1
        while n >= 0:
            nums1[pos] = nums2[n]
            n -= 1
            pos -= 1
# @lc code=end
