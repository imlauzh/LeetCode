#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                # 队尾
                q.pop()
            q.append(i)
            if q[0] <= i - k:  # 最大值不在k范围内
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans

# @lc code=end

