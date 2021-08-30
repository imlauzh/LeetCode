#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        left,right=0,n-1
        while left<=right:
            if left==right:
                return left
            mid=left+(right-left)//2
            if arr[mid]>arr[mid+1]:
                right=mid
            elif arr[mid]<arr[mid+1]:
                left=mid+1
        return -1
# @lc code=end

