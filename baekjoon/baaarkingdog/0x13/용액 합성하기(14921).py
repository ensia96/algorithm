import bisect as B
n, a = int(input()), 2**28
A = [*map(int, input().split())]
for i in range(n):
    l, r = B.bisect_left(A, -A[i], i+1), B.bisect_right(A, -A[i], i+1)
    for j in [l-1, l, r, r+1]:
        if i < j < n:
            a = min(a, A[i]+A[j], key=abs)
print(a)
