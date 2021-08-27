#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
# 快排
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(left, right):
            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]
            index = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[right], nums[index] = nums[index], nums[right]
            return index

        def quickSort(left, right):
            if left >= right:
                return
            mid = partition(left, right)
            quickSort(left, mid-1)
            quickSort(mid+1, right)
        quickSort(0, len(nums)-1)
        return nums


# 堆排序
# 利用下沉构建堆
# 从最后一个非叶子节点往回遍历
# 也就是2i+1=n-1==>i=n/2-1
# 每次把父节点下沉到大的孩子结点位置
# 父节点为i, 则两个孩子结点为2i+1,2i+2
# 升序需要需要大顶堆,降序序列用小顶堆
# 因为堆顶为最大, 所以每次把堆顶与堆的最后一个元素交换
# 然后再把堆顶进行下沉, 重新构建堆
class Solution:
    def heapSort(self, nums: List[int]):
        n = len(nums)
        # 从最后一个非叶子节点执行下沉
        for i in range(n//2 - 1, -1, -1):
            self.shift_down(nums, i, n - 1)
        i = n - 1
        while i > 0:
            # 把堆顶也就是最大值放到最后
            nums[i], nums[0] = nums[0], nums[i]
            # 执行前面数组的下沉，使之符合堆的结构
            i -= 1
            self.shift_down(nums, 0, i)
        return nums

    def shift_down(self, nums, i, end):
        tmp = nums[i]
        while 2 * i + 1 <= end:
            # 左子节点索引
            child = 2 * i + 1
            if child != end and nums[child + 1] > nums[child]:
                child += 1
            if tmp < nums[child]:
                nums[i] = nums[child]
                i = child
            else:
                break
        nums[i] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)


# 归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left, right):
            if left >= right:
                return
            mid = (left+right)//2
            # 注意这里和快排不同
            # 这里的mid是无序的, 所以也需要考虑
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            tmp = []
            # 两部分的起点
            i, j = left, mid+1
            while i <= mid or j <= right:
                # 左边遍历完或者右边的值较小
                if i > mid or (j <= right and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[left:right+1] = tmp
        mergeSort(0, len(nums)-1)
        return nums


# @lc code=start
class Solution:
    def heapSort(self, nums: List[int]):
        n = len(nums)
        # 从最后一个非叶子节点执行下沉
        for i in range(n//2 - 1, -1, -1):
            self.shift_down(nums, i, n - 1)
        i = n - 1
        while i > 0:
            # 把堆顶也就是最大值放到最后
            nums[i], nums[0] = nums[0], nums[i]
            # 执行前面数组的下沉，使之符合堆的结构
            i -= 1
            self.shift_down(nums, 0, i)
        return nums

    def shift_down(self, nums, i, end):
        tmp = nums[i]
        while 2 * i + 1 <= end:
            # 左子节点索引
            child = 2 * i + 1
            if child != end and nums[child + 1] > nums[child]:
                child += 1
            if tmp < nums[child]:
                nums[i] = nums[child]
                i = child
            else:
                break
        nums[i] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)
# @lc code=end
