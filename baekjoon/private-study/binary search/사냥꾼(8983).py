import bisect as B
m, n, l = map(int, input().split())
A, C = sorted(map(int, input().split())), 0
for _ in ' '*n:
    x, y = map(int, input().split())
    C += (y <= l)*bool(B.bisect_left(A, x-l+y) < B.bisect_right(A, x+l-y))
print(C)
