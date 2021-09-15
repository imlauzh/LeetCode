s = 'SSTAARR'
a, b, star, tar, ar, r = '', 0, 0, 0, 0, 0
for c in s[::-1]:
    if c == 'S':
        b = tar-b if a == 'T' else tar
        star = star+b
    elif c == 'T':
        b = ar-b if a == 'A' else ar
        tar = tar+b
    elif c == 'A':
        b = r-b if a == 'R' else r
        ar=ar+b
    else:
        b = 1
        r = r+1
    a = c
print(star)
