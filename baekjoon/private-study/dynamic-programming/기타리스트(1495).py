n, s, m = map(int, input().split())
V = [*map(int, input().split())]
D = [0]*-~m
Q = [(0, s)]
M = -1
for i, v in Q:
    if i == n:
        M = max(M, v)
        continue
    if v-V[i] >= 0 and D[v] == i:
        D[v-V[i]] = i+1
        Q += (i+1, v-V[i]),
    if v+V[i] <= m and D[v] == i:
        D[v+V[i]] = i+1
        Q += (i+1, v+V[i]),
print(M)
