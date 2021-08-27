#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
# 优先队列/大顶堆，每次加入当前窗口内的最大值
# 也就是堆顶元素，判断是否在窗口可以通过下标与窗口左边界
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = [(-nums[i], i) for i in range(k)]
        heapq.heapify(pq)
        res = [-pq[0][0]]
        for i in range(k, n):
            heapq.heappush(pq, (-nums[i], i))
            while pq[0][1] < i-k+1:
                heapq.heappop(pq)
            res.append(-pq[0][0])
        return res

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans
# @lc code=end
