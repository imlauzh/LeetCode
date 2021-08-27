#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr):
        # write code here
        seen = {}
        res = 0
        n = len(arr)
        j = -1
        for i in range(n):
            if arr[i] in seen and j < seen[arr[i]]:
                j = seen[arr[i]]
            seen[arr[i]] = i
            if i-j > res:
                res = i-j
        return res


while True:
    try:
        import sys
        s = Solution()
        lines = str(sys.stdin.readline().strip())
        input_list = list(map(int, lines.split(']')[
                          0].split('[')[-1].split(',')))
        res = s.maxLength(input_list)
        print(f'{res}')
    except:
        break
