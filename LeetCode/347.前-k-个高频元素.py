#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
# 调用包
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        return [i[0] for i in cnt.most_common(k)]


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=collections.Counter(nums)
        heap=[]
        for key,v in cnt.items():
            if len(heap)<k:
                heapq.heappush(heap,(v,key))
            elif v>heap[0][0]:
                heapq.heapreplace(heap,(v,key))
        return [i[1] for i in heap]

# @lc code=end
