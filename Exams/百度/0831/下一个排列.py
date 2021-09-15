# 给一个正整数，输出他的下一个排列


class nextNumber:
    def getNextNumber(self, nums):
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n-1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        elif i == -1:
            return ['-1']
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


c = nextNumber()
a = [1234, 4321, 4312, 2302431]
for i in a:
    i = list(str(i))
    b = c.getNextNumber(i)
    b = int(''.join(b))
    print(b)
