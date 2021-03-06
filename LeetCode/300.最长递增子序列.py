#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# 动态规划
# O(n^2), O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


# 贪心+二分, 单调栈
# 思想: 使得到的递增子序列增长的最慢即可
# 数组 d[i]表示长度为 i 的最长上升子序列的末尾元素的最小值
# 每次都使用二分搜索找第一个比当前数大的位置,替换
# O(nlogn), O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if not stack or stack[-1] < i:
                stack.append(i)
            else:
                left, right = 0, len(stack)-1
                while left <= right:
                    mid = left+(right-left)//2
                    if stack[mid] >= i:
                        # [left, mid-1]
                        index = mid
                        right = mid-1
                    else:
                        # [mid+1, right]
                        left = mid+1
                stack[index] = i
        return len(stack)


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d)-1
                while l <= r:
                    mid = (l+r)//2
                    if d[mid] >= n:
                        # 需要记录当前mid的位置
                        # 作为从右边最靠近n的位置
                        loc = mid
                        r = mid-1
                    else:
                        l = mid+1
                d[loc] = n
        return len(d)
# @lc code=end
