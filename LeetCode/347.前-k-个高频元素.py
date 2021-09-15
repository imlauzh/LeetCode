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
        cnt = collections.Counter(nums)
        pq = []
        # 使用小顶堆，遇到元素先进堆
        # 当堆的大小大于k时
        # 把堆顶也就是最小值pop
        # 这样留下的就是前k大的元素
        for key, v in cnt.items():
            heapq.heappush(pq, (v, key))
            if len(pq) > k:
                heapq.heappop(pq)
        return [i[1] for i in pq]

# @lc code=end
