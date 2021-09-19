l, r = lambda: map(int, input().split()), 0
n, m = l()
b = [[*l()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        r = max(r, b[i][j] + max(sum(b[y][x] for y, x in d if 0 <= y < n and 0 <= x < m)
                                 for d in [((i, j+1), (i, j+2), (i, j+3)), ((i+1, j), (i+2, j), (i+3, j)), ((i, j+1), (i+1, j), (i+1, j+1)), ((i, j+1), (i, j+2), (i+1, j+2)), ((i, j+1), (i, j+2), (i-1, j+2)), ((i+1, j), (i+2, j), (i+2, j+1)), ((i+1, j), (i+2, j), (i+2, j-1)), ((i+1, j), (i, j+1), (i, j+2)), ((i-1, j), (i, j+1), (i, j+2)), ((i, j+1), (i+1, j), (i+2, j)), ((i, j-1), (i+1, j), (i+2, j)), ((i+1, j), (i+1, j+1), (i+2, j+1)), ((i+1, j), (i+1, j-1), (i+2, j-1)), ((i, j+1), (i+1, j+1), (i+1, j+2)), ((i, j+1), (i-1, j+1), (i-1, j+2)), ((i, j+1), (i+1, j+1), (i, j+2)), ((i, j+1), (i-1, j+1), (i, j+2)), ((i+1, j), (i+1, j+1), (i+2, j)), ((i+1, j), (i+1, j-1), (i+2, j))]))
print(r)
