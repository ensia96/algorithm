l, L = lambda: map(int, input().split()), []
_, n = l()
A, B = l(), sorted(l())
for a in A:
    s, e, f = 0, n-1, 0
    while s <= e:
        m = (s+e)//2
        if B[m] > a:
            e = m-1
        elif B[m] < a:
            s = m+1
        else:
            f = 1
            break
    if not f:
        L += [a]
print(len(L))
if L:
    print(*sorted(L))
