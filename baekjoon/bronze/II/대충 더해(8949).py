a, b = input().split()
l = max(len(a), len(b))
a, b = a.zfill(l), b.zfill(l)
for i in range(l):
    print(eval(a[i]+'+'+b[i]), end='')
