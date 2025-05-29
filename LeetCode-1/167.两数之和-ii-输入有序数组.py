#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        n = len(numbers)
        for i in range(n):
            if numbers[i] not in hashmap:
                hashmap[target-numbers[i]] = i+1
            else:
                return [hashmap[numbers[i]], i+1]
        
# @lc code=end

