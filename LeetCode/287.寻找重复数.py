#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
# 哈希表，不过使用了O(n)的空间复杂度
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=[False]*len(nums)
        for num in nums:
            if seen[num]:
                return num
            seen[num]=True

            
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for k, v in count.items():
            if v > 1:
                return k
        return 0


# 二分，不过这里是对1-n进行二分
# 根据数组中小于等于mid的个数
# 来判断重复的整数出现在mid左边还是右边
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while left < right:
            mid = left+(right-left)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                # [left, mid]
                right = mid
            elif count<=mid:
                # [mid+1, right]
                left=mid+1
        return left


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=[False]*len(nums)
        for num in nums:
            if seen[num]:
                return num
            seen[num]=True
# @lc code=end
