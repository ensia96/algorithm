n, m = map(int, input().split())
A = sorted(int(input())for _ in ' '*n)
a, e = 2**31, 0
for s in range(n):
    while e < n and A[e]-A[s] < m:
        e += 1
    if e == n:
        break
    a = min(a, A[e]-A[s])
print(a)
