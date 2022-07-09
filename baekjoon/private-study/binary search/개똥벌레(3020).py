n, h = map(int, input().split())
A, x, c = [[], []], 0, n//2
for i in range(n):
    A[i % 2] += int(input()),
A[0].sort()
A[1].sort()


def f(x, y):
    l, r = 0, c
    while l <= r:
        m = (l+r)//2
        if m == c:
            t = m
            break
        if A[x][m] >= y:
            r, t = m-1, m
        else:
            l = m+1
    return t


T = [c-f(0, i+1)+c-f(1, h-i)for i in range(h)]
print(min(T), T.count(min(T)))
