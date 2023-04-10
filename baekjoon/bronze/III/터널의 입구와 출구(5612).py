n = int(input())
M = m = int(input())
f = 1
for _ in ' '*n:
    x, y = map(int, input().split())
    m += x-y
    M = max(M, m)
    f *= m >= 0
print(M*f)
