#
# @lc app=leetcode.cn id=1095 lang=python3
#
# [1095] 山脉数组中查找目标值
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        # 找峰顶的位置
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                left=mid+1
            else:
                right=mid
        peak=left
        # 左边升序的数组
        left,right=0,peak
        while left<right:
            mid=left+(right-left)//2
            if mountain_arr.get(mid)<target:
                left=mid+1
            else:
                right=mid
        if mountain_arr.get(left)==target:
            return left
        # 右边降序的数组
        left,right=peak,n-1
        while left<right:
            # 由于出现left=mid
            # 所以需要上取整
            mid=left+(right-left+1)//2
            if mountain_arr.get(mid)<target:
                right=mid-1
            else:
                left=mid
        if mountain_arr.get(left)==target:
            return left
        return -1
# @lc code=end

