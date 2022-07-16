m, n, l = map(int, input().split())
A, C = sorted(map(int, input().split())), 0
for _ in ' '*n:
    x, y = map(int, input().split())
    if y > l:
        continue
    s, e, z = 0, len(A)-1, l-y
    while s <= e:
        m = (s+e)//2
        if A[m] < x-z:
            s = m+1
        elif A[m] > x+z:
            e = m-1
        else:
            C += 1
            break
print(C)
