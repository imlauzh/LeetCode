#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        used = [0]*len(nums)
        path=[]

        def backTrack(index):
            if len(path) == len(nums):
                res.append(path[:])
                return
            # 虽然遍历所有的，但是使用一个used数组
            for i in range(len(nums)):
                if used[i]==0:
                    # 前一个如果相同，则当前跳过
                    if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                        continue
                    # 回溯
                    used[i] = 1
                    path.append(nums[i])
                    backTrack(index+1)
                    path.pop()
                    used[i] = 0
        nums.sort()
        backTrack(0)
        return res
# @lc code=end
