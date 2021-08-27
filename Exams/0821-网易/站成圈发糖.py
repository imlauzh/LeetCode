# 小朋友站成一圈发糖，与LeetCode 135类似
# 不过这里是站成一圈


class Solution:
    def calPages(self, ages):
        if len(ages) < 2:
            return 1
        ages.append(ages[0])
        ages.insert(0, ages[-2])
        # print(ages)
        n = len(ages)
        res = [1]*n
        for i in range(1, n):
            if ages[i] > ages[i-1]:
                res[i] = max(res[i], res[i-1]+1)
        for i in range(n-2, -1, -1):
            if ages[i] > ages[i+1]:
                res[i] = max(ages[i+1]+1, res[i])
        res[-2] = max(res[0], res[-2])
        res[1] = max(res[1], res[-1])
        # print(res)
        return sum(res[1:-1])


if __name__ == "__main__":
    import sys
    ages = str(sys.stdin.readline().strip())
    ages = list(map(int, ages.split(' ')))
    s = Solution()
    res = s.calPages(ages)
    print(res)