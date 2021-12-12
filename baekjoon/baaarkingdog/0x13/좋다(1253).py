import bisect as B
n, A = int(input()), sorted(map(int, input().split()))
a = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        k = A[i]-A[j]
        l, r = B.bisect_left(A, k), B.bisect_right(A, k)
        if r-l-(l <= i < r)-(l <= j < r) > 0:
            a += 1
            break
print(a)
