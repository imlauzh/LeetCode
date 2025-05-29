#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        _sum = 0
        for i, num in enumerate(arr):
            _sum += num
            if i<k-1:
                continue
            if _sum>=threshold*k:
                ans+=1
            _sum -= arr[i-k+1]
        return ans 
# @lc code=end

