n = int(input())
S, P = 2**31, (0, 0)
L = [*map(int, input().split())]+[S]
for i in range(n-1):
    l, s, e = L[i], i+1, n
    while s < e:
        m, N = (s+e+1)//2, abs(L[s]+l)
        if abs(L[m]+l) > N:
            e = m-1
        else:
            s = m
    if N < S:
        S, P = N, (l, L[s])
print(*P)
