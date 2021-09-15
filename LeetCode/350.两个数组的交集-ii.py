#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
# 哈希表
# 统计长度小的数组数字的出现次数
# 共同出现减次数并加入到res
# 直到次数为0
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
        res, hashtable = list(), dict()
        for i in nums1:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        for i in nums2:
            if i in hashtable and hashtable[i] > 0:
                res.append(i)
                hashtable[i] -= 1
        return res


# 排序，双指针
# 相等则加入，同时前进
# 不等，增加小的index
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        res=[]
        index1,index2=0,0
        while index1<m and index2<n:
            if nums1[index1]==nums2[index2]:
                res.append(nums1[index1])
                index1+=1
                index2+=1
            elif nums1[index1]>nums2[index2]:
                index2+=1
            else:
                index1+=1
        return res


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        res=[]
        index1,index2=0,0
        while index1<m and index2<n:
            if nums1[index1]==nums2[index2]:
                res.append(nums1[index1])
                index1+=1
                index2+=1
            elif nums1[index1]>nums2[index2]:
                index2+=1
            else:
                index1+=1
        return res
# @lc code=end
