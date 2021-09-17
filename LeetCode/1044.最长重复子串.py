#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#
class Solution:
    def RabinKarpCheck(self, nums, length, n, P, Q):
        visited = set()
        M = P**length % Q
        pre = 0
        # 计算第一个窗口的hash值
        for i in range(length):
            pre = (pre*P+nums[i]) % Q
        visited.add(pre)
        for i in range(length, n):
            # 加上当前位置，减去最开始的位置，类似于滑动窗口
            pre = (pre*P+nums[i]-nums[i-length]*M) % Q
            if pre in visited:
                return i-length+1
            visited.add(pre)
        return -1

    def longestDupSubstring(self, s: str) -> str:
        nums = [ord(c)-ord('a')+1 for c in s]
        P, Q = 131, 2**64
        n = len(s)
        left, right = 0, n
        res = -1
        while left < right:
            # 二分搜索，如果mid长度存在，那么mid+1可能也存在
            # 如果不存在，那么比mid长的也肯定不存在
            mid = left+(right-left)//2
            index = self.RabinKarpCheck(nums, mid, n, P, Q)
            if index != -1:
                left = mid
                res = index
            else:
                right = mid-1
        return s[res:res+left] if res != -1 else ""


# @lc code=start
class Solution:
    def RabinKarpCheck(self, nums, length, n, P, Q):
        visited = set()
        M = P**length % Q
        pre = 0
        for i in range(length):
            pre = (pre*P+nums[i]) % Q
        visited.add(pre)
        for i in range(length, n):
            pre = (pre*P+nums[i]-nums[i-length]*M) % Q
            if pre in visited:
                return i-length+1
            visited.add(pre)
        return -1

    def longestDupSubstring(self, s: str) -> str:
        nums = [ord(c)-ord('a')+1 for c in s]
        P, Q = 131, 2**64
        n = len(s)
        left, right = 0, n
        res = -1
        while left < right:
            mid = left+(right-left)//2
            index = self.RabinKarpCheck(nums, mid, n, P, Q)
            if index != -1:
                left = mid
                res = index
            else:
                right = mid-1
        return s[res:res+left] if res != -1 else ""
# @lc code=end
