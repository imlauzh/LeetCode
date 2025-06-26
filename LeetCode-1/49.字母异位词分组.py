#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 暴力：记录每一种字母异位词
        # 固定的表达方式，一对一 =》 排序？
        hashmap = dict()
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp in hashmap:
                hashmap[tmp].append(s)
            else:
                hashmap[tmp] = [s]
        return list(hashmap.values())
# @lc code=end

