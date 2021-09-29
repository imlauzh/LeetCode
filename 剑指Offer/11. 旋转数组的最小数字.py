class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        n = len(numbers)
        if n == 1:
            return numbers[0]
        left, right = 0, n-1
        while left < right:
            if numbers[left] < numbers[right]:
                return numbers[left]
            mid = left+(right-left)//2
            if numbers[mid] == numbers[right]:
                right -= 1
            elif numbers[mid] > numbers[right]:
                left = mid+1
            else:
                right = mid
        return numbers[left]
