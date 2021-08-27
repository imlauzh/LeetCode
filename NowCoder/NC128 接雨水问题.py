#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self, arr):
        # write code here
        n = len(arr)
        if n < 3:
            return 0
        leftMax = [0]*n
        rightMax = [0]*n
        dp = [0]*n
        leftMax[0] = arr[0]
        rightMax[-1] = arr[-1]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], arr[i])
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], arr[i])

        for i in range(1, n):
            dp[i] = max(0, min(leftMax[i], rightMax[i])-arr[i])
        return sum(dp)
