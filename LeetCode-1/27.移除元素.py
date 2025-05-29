#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
# 双指针，头尾遍历
# 每次循环只操作一个指针
# 

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 统计val的个数
        # 把val移动到后面
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l]==val:
                nums[l] = nums[r]
                r-=1 # 右侧等于val也无妨，下一次循环会覆盖掉
            else: # 只有当左侧指针的值不等于val的时候才进一位
                l+=1
        return l
# @lc code=end

