#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
# 利用set
# O(m+n), O(m+n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)& set(nums2))


# 排序+双指针
# O(mlogm+nlogn), O(logm+logn):排序使用的额外空间
# 主要是空间复杂度降低
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m,n=len(nums1),len(nums2)
        res=[]
        index1,index2=0,0
        while index1<m and index2<n:
            if nums1[index1]==nums2[index2]:
                # 防止重复
                if not res or nums1[index1]!=res[-1]:
                    res.append(nums1[index1])
                index1+=1
                index2+=1
            elif nums1[index1]<nums2[index2]:
                index1+=1
            else:
                index2+=1
        return res

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m,n=len(nums1),len(nums2)
        res=[]
        index1,index2=0,0
        while index1<m and index2<n:
            if nums1[index1]==nums2[index2]:
                if not res or nums1[index1]!=res[-1]:
                    res.append(nums1[index1])
                index1+=1
                index2+=1
            elif nums1[index1]<nums2[index2]:
                index1+=1
            else:
                index2+=1
        return res
# @lc code=end

