#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1

        # 如果窗口大小本身就比数组长度大，则所有元素的k半径平均值都是-1
        if window_size > n:
            return avgs

        current_sum = 0
        # 计算第一个窗口的和 (中心点在 k, 范围是 0 到 2k)
        for i in range(window_size):
            current_sum += nums[i]

        # 计算第一个有效窗口的平均值
        # 第一个中心点是 k，其窗口范围是 [k-k, k+k] -> [0, 2k]
        avgs[k] = current_sum // window_size

        # 滑动窗口计算后续的平均值
        # left_idx_of_window 指的是当前窗口最左边元素的索引
        # center_idx 指的是当前窗口的中心点索引
        # right_idx_of_window 指的是当前窗口最右边元素的索引
        #
        # 当中心点从 k 移动到 k+1 时:
        # 移出窗口的元素是 nums[ (k) - k ] = nums[0]
        # 移入窗口的元素是 nums[ (k+1) + k ] = nums[2k+1]
        #
        # 一般地，当中心点从 center_idx-1 移动到 center_idx 时：
        # 移出窗口的元素是 nums[ (center_idx-1) - k ] = nums[center_idx - k - 1]
        # 移入窗口的元素是 nums[ center_idx + k ]

        # 迭代的中心点从 k+1 开始，到 n-1-k 结束
        for center_idx in range(k + 1, n - k):
            element_leaving = nums[center_idx - k - 1]  # 这是上一个窗口的最左端元素
            element_entering = nums[center_idx + k]  # 这是当前窗口的最右端新元素

            current_sum = current_sum - element_leaving + element_entering
            avgs[center_idx] = current_sum // window_size

        return avgs

# @lc code=end

