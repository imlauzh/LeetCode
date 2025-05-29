#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
# 关键是片段之间需要能够拼接，如果片段之间不连续直接返回-1
# 排序+贪心

# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        sorted_clips = sorted(clips, key=(lambda x: (x[0], x[1])))
        # print(sorted_clips)
        e = sorted_clips[0][0]
        ne = 0
        res = 0
        if e != 0:
            return -1  # 排序后第一个元素起始点不为0，-1
        for i in range(n):
            if sorted_clips[i][0] <= e:
                ne = max(ne, sorted_clips[i][1])
                # print(f"update ne: {ne}")
            elif e < sorted_clips[i][0] < ne:
                res += 1
                e = ne
                ne = max(ne, sorted_clips[i][1])
                # print(f"update res: {res}, {e}")
                if e >= time:
                    return res
            else:
                return -1
            if ne >= time:
                return res+1
        return -1
# @lc code=end

