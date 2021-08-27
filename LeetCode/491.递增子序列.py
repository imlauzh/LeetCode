#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subSeq=[]
        def backTrack(index,last):
            if index==len(nums):
                if len(subSeq)>1:
                    res.append(subSeq[:])
                return
            if nums[index]>=last:
                subSeq.append(nums[index])
                backTrack(index+1,nums[index])
                subSeq.pop()
            # 不选择当前数字的情况：当前元素比之前保存的最后的元素小
            if nums[index]!=last:
                backTrack(index+1,last)
            
        backTrack(0,float('-inf'))
        return res
# @lc code=end

