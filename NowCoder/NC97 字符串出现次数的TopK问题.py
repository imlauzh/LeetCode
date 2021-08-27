#
# return topK string
# @param strings string字符串一维数组 strings
# @param k int整型 the k
# @return string字符串二维数组
#
class Solution:
    def topKstrings(self, strings, k):
        # write code here
        import collections
        import heapq
        count = collections.Counter(strings)
        pq = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(pq)

        res = []
        for _ in range(k):
            freq, word = heapq.heappop(pq)
            res.append([word, -freq])
        return res


class Solution:
    def topKstrings(self, strings, k):
        # write code here
        count = {}
        for i in strings:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        bucket = {}
        for word, freq in count.items():
            if freq in bucket:
                bucket[freq].append(word)
            else:
                bucket[freq] = [word]
        keys = sorted(bucket.keys(), reverse=True)
        res, cnt = [], 0
        while True:
            for freq in keys:
                strs = sorted(bucket[freq])
                for word in strs:
                    cnt += 1
                    res.append([word, freq])
                    if cnt == k:
                        return res
