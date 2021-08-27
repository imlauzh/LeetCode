#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self, nums, target):
        # write code here
        n = len(nums)
        left, right = 0, n-1
        loc = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                loc = mid
                break
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if loc == -1:
            return loc
        while loc-1 >= 0 and nums[loc-1] == target:
            loc -= 1
        return loc
