#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
# 快速选择
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot = random.randint(l, r)
            nums[r], nums[pivot] = nums[pivot], nums[r]
            idx = l
            for i in range(l, r):
                if nums[i] > nums[r]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                    idx += 1
            nums[r], nums[idx] = nums[idx], nums[r]
            return idx

        def qselect(l, r):
            if l >= r:
                return
            mid = partition(l, r)
            if mid == k-1:
                return
            elif mid < k-1:
                qselect(mid+1, r)
            else:
                qselect(l, mid-1)
        qselect(0, len(nums)-1)
        print(nums)
        return nums[k-1]


# heapq 调包
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            # 将 item 的值加入 heap 中，保持堆的不变性。
            # 维护一个最小堆
            heapq.heappush(heap, num)
            # 堆的大小超过k，就把最小的pop，保留大的
            # 这样就留下前k个大的
            if len(heap) > k:
                # 把小根堆堆顶pop
                heapq.heappop(heap)
        return heap[0]


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        寻找第k个大的元素第一想法是构建小顶堆
        '''
        def shift_up(new_idx):
            new_val = minheap[new_idx]  # 临时存储需要上浮的元素
            # 向上寻找父结点进行比较，决定是否上浮
            while new_idx > 0 and minheap[(new_idx-1)//2] > new_val:
                minheap[new_idx] = minheap[(new_idx-1)//2]  # 父结点下沉
                new_idx = (new_idx-1) // 2  # 子结点坐标上移
            minheap[new_idx] = new_val  # 完成结点上浮

        def shift_down(start, end):
            start_val = minheap[start]  # 临时存储头节点
            # 向下寻找双子结点进行比较，决定是否下沉
            while start*2 + 1 <= end:
                child = start*2 + 1  # 设置左子节点
                # 比较左右子节点的大小，对于小顶堆来说，需要找出最小子结点
                if child+1 <= end and minheap[child] > minheap[child+1]:
                    child += 1
                if minheap[child] < start_val:
                    minheap[start] = minheap[child]  # 子结点上浮
                    start = child
                else:
                    break
            minheap[start] = start_val  # 完成结点下沉

        # 上浮式建堆
        minheap = []
        # 1 <= k <= nums.length <= 104
        for i in range(k):
            minheap.append(nums[i])
            shift_up(i)

        # 下沉式维护
        for num in nums[k:]:
            if num > minheap[0]:
                minheap[0] = num
                shift_down(0, k-1)

        return minheap[0]
# @lc code=end
