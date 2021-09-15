#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
# 每次找最大的元素，两次翻转就可以放到最后
# 第一次翻转最大元素index+1, 第二次翻转全部长度
# 递归法
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        res = []
        idx = arr.index(max(arr))
        arr = arr[:idx+1][::-1] + arr[idx+1:]
        arr = arr[::-1]
        res += [idx+1, len(arr)]
        temp = self.pancakeSort(arr[:-1])
        res = res + temp
        return res


# 迭代法
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        length = len(arr)
        while length > 0:
            idx = arr.index(max(arr[:length]))
            # 第一次翻转
            arr = arr[:idx+1][::-1] + arr[idx+1:]
            res.append(idx+1)
            # 第二次翻转
            arr = arr[:length][::-1]
            res.append(length)
            length -= 1
        return res


# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        while len(arr) > 1:
            maxIdx, maxVal = 0, float('-inf')
            for j in range(len(arr)):
                if arr[j] > maxVal:
                    maxVal = arr[j]
                    maxIdx = j
            if maxIdx == 0:
                res.append(len(arr))
                arr = arr[::-1][:-1]
            else:
                res.extend([maxIdx+1, len(arr)])
                arr = arr[:maxIdx+1][::-1]+arr[maxIdx+1:]
                arr = arr[::-1][:-1]
        return res
# @lc code=end
