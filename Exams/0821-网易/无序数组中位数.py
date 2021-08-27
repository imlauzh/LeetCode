
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可


# @param arr float浮点型一维数组 非空无序数组
# @return float浮点型

# 无序数组中位数

class Solution:
    def median(self, arr):
        # write code here
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def partition(l, r):
            pivot = arr[r]
            idx = l
            for i in range(l, r):
                if arr[i] < pivot:
                    swap(idx, i)
                    idx += 1
            swap(idx, r)
            return idx

        def qselect(l, r, k):
            if l >= r:
                return
            mid = partition(l, r)
            if mid == k-1:
                return
            elif mid > k-1:
                qselect(l, mid-1, k)
            else:
                qselect(mid+1, r, k)
        n = len(arr)
        qselect(0, n-1, (n+1)//2)
        print(arr[n//2])
        print(arr[n//2-1])
        return arr[n//2] if n % 2 != 0 else (arr[n//2-1]+arr[n//2])/2


s = Solution()
i = [1, 2, 3, 4]
res = s.median(i)
print(res)
