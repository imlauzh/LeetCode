#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
# next
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def nextPermutation(nums):
            n = len(nums)
            i = n-2
            while i >= 0 and nums[i] >= nums[i+1]:
                i -= 1
            if i >= 0:
                j = n-1
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            left, right = i+1, n-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        res = []
        n = len(nums)
        nums.sort()
        for _ in range(math.factorial(n)):
            res.append(nums.copy())
            nextPermutation(nums)
        return res


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index=0):
            # 所有数都填完了
            if index == n:
                res.append(nums[:])
            for i in range(index, n):
                # 动态维护数组
                nums[index], nums[i] = nums[i], nums[index]
                # 继续递归填下一个数
                backtrack(index + 1)
                # 撤销操作
                nums[index], nums[i] = nums[i], nums[index]

        n = len(nums)
        res = []
        backtrack(0)
        return res
# @lc code=end
