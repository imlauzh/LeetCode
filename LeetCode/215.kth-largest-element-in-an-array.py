#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (60.16%)
# Likes:    6305
# Dislikes: 382
# Total Accepted:    966.3K
# Total Submissions: 1.6M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# 快速排序中的快速选择算法：当分区返回的index等于要求的k时，可以直接输出第k个元素
#
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            # 随机选择一个基准值
            pivot = random.randint(l, r)
            # 基准放到最右边
            nums[pivot], nums[r] = nums[r], nums[pivot]
            i = l
            for j in range(l, r):
                # 遍历，大于基准放到左边，因为是求第k大的元素
                if nums[j] > nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            # 基准放回
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def qselect(nums, l, r, k):
            if l >= r:
                return
            mid = partition(nums, l, r)
            # 分区基准等于k-1，也就是基准前有k-1个元素比基准大
            # 也就是基准值是第k大的元素
            if mid == k-1:
                return
            # 如果前面元素多于k-1，那么在前一个分区找就可以
            elif mid > k-1:
                qselect(nums, l, mid-1, k)
            # 少于k-1，同理
            else:
                qselect(nums, mid+1, r, k)
        qselect(nums, 0, len(nums)-1, k)
        return nums[k-1]
# @lc code=end
