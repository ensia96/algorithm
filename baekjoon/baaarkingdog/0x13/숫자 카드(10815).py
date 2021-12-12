n = int(input())
C = sorted(map(int, input().split()))
_, A = input(), []
for k in map(int, input().split()):
    s, e, f = 0, n-1, 0
    while s <= e:
        m = (s+e)//2
        if C[m] < k:
            s = m+1
        elif C[m] > k:
            e = m-1
        else:
            f = 1
            break
    A += [f]
print(*A)
