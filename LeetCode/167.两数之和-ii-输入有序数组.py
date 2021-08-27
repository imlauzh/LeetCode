#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
# 
# 非常巧妙地思想
# 从两边向里收缩，两个数分布在数组两头
# 因为是升序，正好就是两数和的分布的中间
# 大了就缩小r，小了就增大l

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l,r=0,n-1
        while l<r:
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                return [l+1,r+1]
        return -1
# @lc code=end

