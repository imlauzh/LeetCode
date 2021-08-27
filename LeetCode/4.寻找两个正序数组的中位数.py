#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
# 题目要求我们找的是中位数，由于中位数存在一个边界情况：
# 奇数时取中间，偶数时取中间两个数除2.
# 故我们可以先实现一个找第k小数的办法。

# 对于两个有序数组，我们要找第k小的数
# 由于时间复制度要求是log，所以自然的想法就是对两个数组每次切一半。
# 好，假设我们取两个数组k/2位置上的数(这里暂时不考虑上溢)
# 如果nums1[k/2]>=nums2[k/2]，这意味着：
# nums2数组的左半边都不需要考虑了，因为肯定会比第k小的数要来得小。
# 所以我们可以切掉nums2数组的一半，如此递归，每次都能切走一半
# 自然能达到O（log(m+n)）复杂度的要求了。
# 在具体的代码实现中，为了方便处理边界情况，
# 我们可以令nums1始终是长的那个数组，
# 然后令t = min(k//2,len(nums2))便可以防止上溢的发生。

# 令 k1 = ( len(nums1) + len(nums2) + 1 ) // 2
# 令 k2 = ( len(nums1) + len(nums2) + 2 ) // 2
# 对于偶数情况，k1对应中间左边，k2对应中间右边
# 对于奇数情况，k1，k2都对应中间
# 所以我们得到了获得中位数的统一方法：(helper(k1)+helper(k2))/2

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def helper(nums1, nums2, k):
            if(len(nums1) < len(nums2)):
                nums1, nums2 = nums2, nums1  # 保持nums1比较长
            if(len(nums2) == 0):
                return nums1[k-1]  # 短数组空，直接返回
            if(k == 1):
                return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
            t = min(k//2, len(nums2))  # 保证不上溢
            if(nums1[t-1] >= nums2[t-1]):
                return helper(nums1, nums2[t:], k-t)
            else:
                return helper(nums1[t:], nums2, k-t)
        m, n = len(nums1), len(nums2)
        k1 = (m + n + 1) // 2
        k2 = (m + n + 2) // 2
        return (helper(nums1, nums2, k1) + helper(nums1, nums2, k2)) / 2
# @lc code=end
