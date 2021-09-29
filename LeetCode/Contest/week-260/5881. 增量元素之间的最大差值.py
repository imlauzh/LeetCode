from typing_extensions import Required


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        rightMax=[0]*n
        rightMax[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(nums[i],rightMax[i+1])
        res=-1
        for i in range(n):
            res=max(res,rightMax[i]-nums[i]) if rightMax[i]>nums[i] else res
        return res
