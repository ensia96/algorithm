n, m = map(int, input().split())
A = [*map(int, input().split())]
s, j, c = A[0], 1, 0
for i in range(n):
    while j < n and s < m:
        s, j = s+A[j], j+1
    c, s = c+(s == m), s-A[i]
print(c)
