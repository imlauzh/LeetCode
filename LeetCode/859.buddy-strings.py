#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, g: str) -> bool:
        if len(s)!=len(g):return False
        if s==g:
            seen=set()
            for i in s:
                if i in seen:
                    return True
                seen.add(i)
            return False
        else:
            pairs=[]
            for a,b in zip(s,g):
                if a!=b:
                    pairs.append((a,b))
                if len(pairs)>2:return False
            return len(pairs)==2 and pairs[0]==pairs[1][::-1]
# @lc code=end

