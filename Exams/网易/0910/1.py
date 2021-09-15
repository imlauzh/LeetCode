# 插入两个字符成为回文串
class HuiWen:
    def calc(self, str1):
        import collections
        cnt = collections.Counter(str1)
        ans = 0
        for i in cnt.items():
            if cnt[i] % 2 != 0:
                ans += 1
        if ans > 2:
            return 0
        return 1


hw = HuiWen()
s = input().strip()
res = hw.calc(s)
print(res)
