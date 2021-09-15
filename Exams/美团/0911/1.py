"""
12221
子串可以整除22的个数
"""


class Divs:
    def calc(self, n, s):
        def check(num):
            if num % target == 0:
                return True
            return False
        target = 22
        res = 0
        for i in range(n-2):
            right = i
            while right < n:
                while right < n and int(s[right]) % 2 != 0:
                    right += 1
                if right>=n:
                    break
                num = int(s[i:right+1])
                # print(num)
                if num < target:
                    right+=1
                    continue
                if check(num):
                    res += 1
                right += 1
        return res
    def calc1(self,n,s):
        res=0
        for i in range(n):
            for j in range(i,n):
                if int(s[i:j+1])%22==0:
                    res+=1
        return res

d = Divs()
s = input().strip()
n = len(s)
res = d.calc1(n, s)
print(res)
