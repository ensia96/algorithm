n, m = int(input()), int(input())
M, T = [], [1]*m
for i in range(m):
    a, b = map(int, input().split())
    M += [(a, b, i)]if a < b else[(a-n, b, i), (a, b+n, i)]
M.sort(key=lambda x: (x[0], -x[1]))
t = M[0][1]-1
for x, y, z in M:
    if t < y:
        t = y
    else:
        T[z] = 0
print(*[i+1 for i in range(m)if T[i]])
