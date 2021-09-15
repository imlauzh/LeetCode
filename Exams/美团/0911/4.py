"""
周期序列
"""
s = input().strip()
times = int(input().strip())
for _ in range(times):
    n, k = list(map(int, input().strip().split()))
    if k > len(s):
        print(-1)
        continue
    if n > len(s):
        n = len(s)
    news = s[:n]
    tmp = [len(news)]
    for i in range(1, n):
        flag = True
        for j in range(n):
            if i+j < n:
                if s[j] != s[j+i]:
                    flag = False
                    break
        if flag:
            tmp.append(i)
    tmp.sort()
    if k-1 < len(tmp):
        print(tmp[k-1])
    else:
        print(-1)
