n, k = map(int, input().split())
i = s = 0
while 1:
    m, i = 9*(i+1)*10**i, i+1
    if k <= m:
        break
    k, s = k-m, s+m//i
f = k % i
t = s+k//i+bool(f)
print([str(t)[f-1], -1][t > n])
