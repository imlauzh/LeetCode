"""
5
1 3 5 2 4
3
4 2 7
"""

class BookLocation:
    def calc(self, n, nums, m, b):
        intervals = [[]]*n
        last = 1
        for i in range(n):
            intervals[i] = [last, last+nums[i]]
            last += nums[i]
        # print(intervals)
        res = []
        # for j in range(m):
        #     for i in range(n):
        #         if intervals[i][0]<=b[j]<intervals[i][1]:
        #             # print(intervals[i],b[j],i+1)
        #             res.append(i+1)
        loc = dict()
        for j in range(m):
            loc[b[j]] = 0
        b.sort()
        j = 0
        for i in range(n):
            while j < m and intervals[i][0] <= b[j] < intervals[i][1]:
                loc[b[j]] = i+1
                j += 1
        for r in b:
            print(loc[r])

    def calc1(self, n, nums, m, b):
        intervals = []
        last = 0
        for i in range(n):
            intervals.append(last+nums[i])
            last += nums[i]
        for j in range(m):
            left = 0
            right = n-1
            book = b[j]
            res = 0
            while left <= right:
                mid = left+(right-left)//2
                if intervals[mid] == book:
                    res = mid
                    break
                elif intervals[mid] < book:
                    left = mid+1
                else:
                    res = mid
                    right = mid-1
            print(res+1)


bl = BookLocation()
n = int(input().strip())
nums = list(map(int, input().strip().split(' ')))
m = int(input().strip())
b = list(map(int, input().strip().split(' ')))
bl.calc1(n, nums, m, b)
