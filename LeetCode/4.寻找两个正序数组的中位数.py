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


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newIdx1 = min(index1+k//2-1, m-1)
                newIdx2 = min(index2+k//2-1, n-1)
                if nums1[newIdx1] <= nums2[newIdx2]:
                    k -= newIdx1-index1+1
                    index1 = newIdx1+1
                else:
                    k -= newIdx2-index2+1
                    index2 = newIdx2+1

        m, n = len(nums1), len(nums2)
        total = m+n
        if total % 2 == 1:
            return getKthElement((total+1)//2)
        else:
            return (getKthElement(total//2+1)+getKthElement(total//2))/2
