#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
# 关键：当一个湖第二次下雨时，寻找这个湖前一次下雨之后的第一个可用的晴天

# @lc code=start
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 字典存放湖下雨日期
        lakes=collections.defaultdict(collections.deque)
        for idx,lake in enumerate(rains):
            if lake!=0:
                lakes[lake].append(idx)
        # 最小堆
        queue=[]
        flood=set()
        res=[]
        for idx,lake in enumerate(rains):
            if lake!=0:
                if lake in flood:
                    return []
                else:
                    res.append(-1)
                    flood.add(lake)
                    lakes[lake].popleft()
                    if lakes[lake]:
                        heapq.heappush(queue,lakes[lake][0])
            else:
                if not queue:
                    res.append(1)
                else:
                    index=heapq.heappop(queue)
                    res.append(rains[index])
                    flood.remove(rains[index])
        return res
# @lc code=end

