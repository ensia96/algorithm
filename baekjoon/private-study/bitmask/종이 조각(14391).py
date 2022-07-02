n, m = map(int, input().split())
A = [input()for _ in ' '*n]
N, M = range(n), range(m)
r = 0
for k in range(1 << m*n):
    t = 0
    for i in N:
        x = '0'
        for j in M:
            if k & 1 << i*m+j:
                x += A[i][j]
            else:
                t, x = t+int(x), '0'
        t += int(x)
    for j in M:
        x = '0'
        for i in N:
            if k & 1 << i*m+j:
                t, x = t+int(x), '0'
            else:
                x += A[i][j]
        t += int(x)
    r = max(r, t)
print(r)
