n = int(input())
L = [*map(int, input().split())]
S, P = 2**31, 0
for i in range(n-1):
    l, s, e = L[i], i+1, n-1
    while s < e:
        m = (s+e+1)//2
        if L[m] > -l:
            e = m-1
        else:
            s = m
    r = abs(l+L[s])
    if r < S:
        S, P = r, (l, L[s])
print(*P)
