#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        ret=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            # 滑动窗口包含了所有T元素
            if needCnt==0:
                # i右移，排除多余元素
                while True:
                    c=s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<ret[1]-ret[0]:
                    ret=(i,j)
                # i右移1个位置，寻找新的满足条件滑动窗口
                need[s[i]]+=1
                needCnt+=1
                i+=1
        return '' if ret[1]>len(s) else s[ret[0]:ret[1]+1]
# @lc code=end

