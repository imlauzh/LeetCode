#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
# next
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
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
        nums=[]
        for i in range(n):
            nums.append(str(i+1))
        for i in range(k-1):
            nextPermutation(nums)
        return ''.join(nums)


# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)
# @lc code=end

