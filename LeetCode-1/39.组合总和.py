#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if candidates[0] > target:
            return []
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left==0:
                ans.append(path.copy())
                return
            if i==len(candidates) or left<candidates[i]:
                return
            
            dfs(i+1, left)

            path.append(candidates[i])
            dfs(i, left-candidates[i])
            path.pop()

        dfs(0, target)
        return ans

# @lc code=end



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            # 枚举选哪个
            for j in range(i, len(candidates)):
                if candidates[j] > left:  # 排序了，后面的数都太大
                    break
                path.append(candidates[j])
                dfs(j, left - candidates[j])
                path.pop()  # 恢复现场

        dfs(0, target)
        return ans
    
