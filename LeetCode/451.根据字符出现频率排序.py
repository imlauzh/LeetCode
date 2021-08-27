#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
# 桶排序
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        bucket = [[] for _ in range(len(s)+1)]
        for k, v in cnt.items():
            bucket[v].append(k)
        res = ""
        for i in range(len(s), -1, -1):
            if len(bucket[i]) == 0:
                continue
            for j in bucket[i]:
                res += j*i
        return res


# @lc code=start
# 堆排序, hash表
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        pq = []
        for k, v in cnt.items():
            heapq.heappush(pq, (-v, ord(k), k))
        ans = []
        while pq:
            repeats, _, char = heapq.heappop(pq)
            ans.append(char*-repeats)
        return ''.join(ans)
# @lc code=end
