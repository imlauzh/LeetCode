#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
class Solution:
    def MySort(self, arr):
        # write code here
        return self.quick_sort(arr)
    
    def bubble_sort(self, arr):
        # 冒泡排序 不通过
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
        
    def select_sort(self, arr):
        # 选择排序 不通过
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr
     
    def insert_sort(self, arr):
        # 插入排序 不通过
        for i in range(1, len(arr)):
            tmp = arr[i]                     # tmp要插入的之
            j = i - 1
            while j >= 0 and arr[j] > tmp:   # 前面的值比tmp大
                arr[j+1] = arr[j]             # 前面的值向后移一位
                j = j - 1                   # 继续向前对比
            arr[j+1] = tmp                   # 直到while不满足条件, 也就是前面的值比tmp小, 插入到比tmp小的值后
        return arr
     
    def quick_sort(self, arr):
        # 快速排序 通过
        if len(arr) < 2:
            return arr
        else:
            tmp = arr[0]
            less = [i for i in arr[1:] if i <= tmp]
            more = [i for i in arr[1:] if i > tmp]
            return self.quick_sort(less) + [tmp] + self.quick_sort(more)
         
    def merge_sort(self, arr):
        # 归并排序 可能通过 可能不通过
        if len(arr) < 2:
            return arr
        else:
            num = len(arr) // 2
            left = self.merge_sort(arr[:num])
            right = self.merge_sort(arr[num:])
            return self.merge(left, right)
         
    def merge(self, left, right):
        l,r = 0,0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result
