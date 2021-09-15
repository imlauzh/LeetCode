# 两个升序数组找第k个最小的数
class Smallk:
    def calc(self,nums1,nums2,k):
        index1, index2 = 0, 0
        m,n=len(nums1),len(nums2)
        while True:
            # 特殊情况
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # 正常情况
            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1


al=Smallk()
lines=input().strip()
lines=lines.split('],')
k=int(lines[2])
print(lines[0])
l1=list(map(int,lines[0].strip('[').split(',')))
l2=list(map(int,lines[1].strip('[').split(',')))
res=al.calc(l1,l2,k)
print(res)
