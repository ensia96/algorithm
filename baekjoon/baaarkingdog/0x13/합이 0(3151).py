import bisect as B
l, r = B.bisect_left, B.bisect_right
n, a = int(input()), 0
A = sorted(map(int, input().split()))
for i in range(n):
    for j in range(i+1, n):
        s = A[i]+A[j]
        a += r(A, -s, j+1) != l(A, -s, j+1)
print(a)
