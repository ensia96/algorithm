n, m = map(int, input().split())
A, a, C = [], 10**9, [0]*n
c = i = 0
for y in range(n):
    A += [(int(x), y)for x in input().split()]
A.sort()
for j in range(n*m):
    s, b = A[j]
    c, C[b] = c+(not C[b]), C[b]+1
    while c == n:
        x, y = A[i]
        a, C[y] = min(a, s-x), C[y]-1
        i, c = i+1, c-(not C[y])
print(a)
