class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0]*n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(pre[i-1], nums[i])
        suf = [0]*n
        suf[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        res = 0
        for i in range(1, n-1):
            if pre[i-1] < nums[i] < suf[i+1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
        return res
