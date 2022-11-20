def f(i, j):
    for x, y in [(i-1, j), (i, j-1), (i, j), (i, j+1), (i+1, j)]:
        if 0 <= x < 10 > y >= 0:
            T[x][y] = not T[x][y]
    return 1


A = [[i == 'O'for i in input()]for _ in ' '*10]
C = [101 for _ in range(1 << 10)]
for i in range(1 << 10):
    T = [A[i][:]for i in range(10)]
    c = sum(i & 1 << j and f(0, j)for j in range(10)) + \
        sum(T[x-1][y] and f(x, y)for x in range(1, 10)for y in range(10))
    if not any(sum(t)for t in T):
        C[i] = c
z = min(C)
print(z if z-101 else -1)
