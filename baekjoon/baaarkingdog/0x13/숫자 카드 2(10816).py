n = int(input())
A = sorted(map(int, input().split()))
_, a = input(), []
for b in map(int, input().split()):
    s, e = S, E = 0, n
    while s < e:
        m = (s+e)//2
        if A[m] >= b:
            e = m
        else:
            s = m+1
    while S < E:
        m = (S+E)//2
        if A[m] > b:
            E = m
        else:
            S = m+1
    a += [S-s]
print(*a)
