import sys
I = sys.stdin.readline
n, m = map(int, I().split())
n += 1
C, V = [[]for _ in ' '*n], [0]*n
for _ in ' '*m:
    u, v = map(int, I().split())
    C[u].append(v)
    C[v].append(u)
for i in range(1, n):
    if V[i]:
        continue
    q, V[i] = [i], 1
    m += 1
    for p in q:
        for c in C[p]:
            if not V[c]:
                V[c] = 1
                m -= 1
                q += [c]
print(m-1)
