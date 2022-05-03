n, s, m = map(int, input().split())
V = [*map(int, input().split())]
Q = [(0, s)]
M = -1
for i, v in Q:
    if i == n:
        M = max(M, v)
        continue
    if v-V[i] >= 0:
        Q += (i+1, v-V[i]),
    if v+V[i] <= m:
        Q += (i+1, v+V[i]),
print(M)
