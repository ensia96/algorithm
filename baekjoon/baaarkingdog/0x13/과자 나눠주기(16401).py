M, _ = map(int, input().split())
L = [*map(int, input().split())]
s, e, f = 1, max(L), 0
while s < e:
    m = (s+e+1)//2
    if sum(l//m for l in L) >= M:
        s, f = m, 1
    else:
        e = m-1
print(s if f else 0)
