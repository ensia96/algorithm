n = int(input())
m = int(input())
A = sorted(map(int, input().split()))
c, l, r = 0, 0, n-1
while l < r:
    t = A[l]+A[r]
    r -= t >= m
    l += t <= m
    c += t == m
print(c)
