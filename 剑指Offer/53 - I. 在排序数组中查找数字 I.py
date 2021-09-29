class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = -1, -1
        for i in range(len(nums)):
            if start == -1 and nums[i] == target:
                start = i
                end = i
            elif nums[i] == target:
                end = i
        return end-start+1 if start != -1 else 0


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect_right(nums, target)-bisect_left(nums, target)
