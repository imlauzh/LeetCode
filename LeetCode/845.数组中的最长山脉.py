#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        left,res=0,0
        # 山脉长度需要大于2
        while left+2<n:
            right=left+1
            if arr[left+1]>arr[left]:
                while right+1<n and arr[right+1]>arr[right]:
                    right+=1
                if right+1<n and arr[right+1]<arr[right]:
                    while right+1<n and arr[right+1]<arr[right]:
                        right+=1
                    res=max(res,right-left+1)
                # 不满足下山，下一个元素越界或者是相等，需要跳过
                else:
                    right+=1
            # 山脉与山脉之间的是相同的
            left=right
        return res
# @lc code=end
