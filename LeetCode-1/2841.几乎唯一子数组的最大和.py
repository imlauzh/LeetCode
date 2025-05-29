#
# @lc app=leetcode.cn id=2841 lang=python3
#
# [2841] 几乎唯一子数组的最大和
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        n = len(nums)
        cur_sum = 0
        cur_set = defaultdict(int)
        for idx, num in enumerate(nums):
            cur_sum += num
            cur_set[num] += 1
            if idx < k - 1:
                continue
            if len(cur_set) >= m:
                ans = max(ans, cur_sum)
            leave_num = nums[idx - k + 1]
            cur_sum -= leave_num
            if cur_set[leave_num] == 1:
                cur_set.pop(leave_num)
            else:
                cur_set[leave_num] -= 1
        return ans

# @lc code=end

