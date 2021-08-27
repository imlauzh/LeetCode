#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)


# 贪心+二分
# 思想: 使得到的递增子序列增长的最慢即可
# 每次都使用二分搜索找第一个比当前数大的位置,替换
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d=[]
        for n in nums:
            if not d or n>d[-1]:
                d.append(n)
            else:
                l,r=0,len(d)-1
                while l<=r:
                    mid=(l+r)//2
                    if d[mid]>=n:
                        # 需要记录当前mid的位置
                        # 作为从右边最靠近n的位置
                        loc=mid
                        r=mid-1
                    else:
                        l=mid+1
                d[loc]=n
        return len(d)
# @lc code=end

