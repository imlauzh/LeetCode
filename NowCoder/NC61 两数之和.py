#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
#
class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        ret=[]
        dicts={}
        for i,val in enumerate(numbers):
            tmp=target-val
            if tmp in dicts:
                return [dicts[tmp]+1,i+1]
            dicts[val]=i

while True:
    try:
        import sys
        s = Solution()
        lines = str(sys.stdin.readline().strip())
        target = int(lines.split(',')[-1])
        numbers = list(map(int, lines.split(']')[0].split('[')[-1].split(',')))
        res = s.twoSum(numbers, target)
        print(f'[{res[0]},{res[1]}]')
    except:
        break