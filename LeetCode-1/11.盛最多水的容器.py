#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
# 尝试移动指向较短板的那个指针。例如，如果 height[left] < height[right]，我们就将 left 指针向右移动 (left += 1)。这样做是期望找到一个更高的 height[left+1]，从而有可能形成一个更大的储水面积，尽管宽度减小了。
# 剪枝对延时比较重要

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0  # 1. 初始化最大面积 (res) 为 0
        left, right = 0, len(height) - 1  # 2. 初始化左右指针，分别指向数组的最左端和最右端
        maxh = max(height) # 3. 预计算数组中的最大高度，用于后续的优化判断

        # 4. 当左指针小于右指针时，持续循环（即容器宽度大于0）
        while left < right:
            # 5. 判断左右指针指向的高度哪个更小
            if height[left] <= height[right]:
                # 6. 如果左边的高度更小或相等，则容器的有效高度由左边决定
                #    计算当前形成的容器面积，并与已知的最大面积 res 比较，取较大者
                res = max(res, height[left] * (right - left))
                # 7. 移动左指针向右。为什么移动左指针？
                #    因为当前容器的面积受限于左边较短的板 height[left]。
                #    宽度 (right - left) 已经确定。如果想找到更大的面积，
                #    在宽度必然减小或不变（如果只移动短板）的情况下，必须期望高度增加。
                #    移动短板 height[left] 才有可能使得 min(height[new_left], height[right]) 变大。
                #    如果移动长板 height[right]，新的高度 min(height[left], height[new_right]) 
                #    仍然会受限于 height[left]，但宽度却减小了，面积必然不会更大。
                left += 1
            else: # height[left] > height[right]
                # 8. 如果右边的高度更小，则容器的有效高度由右边决定
                #    计算当前形成的容器面积，并与已知的最大面积 res 比较，取较大者
                res = max(res, height[right] * (right - left))
                # 9. 移动右指针向左。理由同上，移动短板（这里是右板）才有可能找到更大的面积。
                right -= 1
            
            # 10. 这是一个重要的剪枝优化：
            #     如果当前已找到的最大面积 res 已经大于
            #     “数组中的最大可能高度 (maxh)” 乘以 “当前左右指针形成的宽度 (right - left)”
            #     这意味着，即使后续找到的两条线都是数组中最高的那条线 (maxh)，
            #     它们形成的面积也不可能超过当前已经找到的 res，因为宽度 (right - left) 只会继续减小。
            #     所以可以直接跳出循环。
            if res > maxh * (right - left): # 注意：这里的 (right - left) 是指针移动后的新宽度
                break
        
        # 11. 返回找到的最大面积
        return res
# @lc code=end

