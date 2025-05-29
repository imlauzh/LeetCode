#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() # 记录补充的位置
        for i in range(len(nums)):
            if nums[i] not in hashmap: 
                hashmap[target-nums[i]] = i
            else:
                return [hashmap[nums[i]], i]
# @lc code=end

