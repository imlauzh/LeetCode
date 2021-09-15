#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        need=collections.Counter(t)
        needcnt=len(t)
        left,res=0,(0,n)
        for right in range(n):
            if need[s[right]]>0:
                needcnt-=1
            need[s[right]]-=1
            # 滑动窗口包含了所有T元素
            if needcnt==0:
                # i右移，排除多余元素
                while True:
                    # 碰到t中需要的字符，退出循环
                    if need[s[left]]==0:
                        break
                    need[s[left]]+=1
                    left+=1
                # 更新结果
                if right-left<res[1]-res[0]:
                    res=(left,right)
                # i右移1个位置，寻找新的满足条件滑动窗口
                need[s[left]]+=1
                needcnt+=1
                left+=1
        return '' if res[1]>len(s)-1 else s[res[0]:res[1]+1]


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=collections.Counter(t)
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

