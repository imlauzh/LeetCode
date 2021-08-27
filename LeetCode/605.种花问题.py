#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
# https://leetcode-cn.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (33.56%)
# Likes:    361
# Dislikes: 0
# Total Accepted:    98.2K
# Total Submissions: 292.8K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 
# 给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n
# ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# flowerbed[i] 为 0 或 1
# flowerbed 中不存在相邻的两朵花
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(len(flowerbed)):
            if i==0 or i==len(flowerbed)-1:
                continue
            if flowerbed[i]==0:
                if(flowerbed[i-1]+flowerbed[i+1]==0):
                    cnt+=1
                    flowerbed[i]=1
        return cnt>=n
# @lc code=end

