import sys
sys.setrecursionlimit(10**9)
I = sys.stdin.readline
n, r, q = map(int, I().split())
C, T = [[]for _ in ' '*(n+1)], [0]*(n+1)
for _ in ' '*(n-1):
    u, v = map(int, I().split())
    C[u].append(v)
    C[v].append(u)


def D(c): T[c] = 1; T[c] += sum(not T[n] and D(n)for n in C[c]); return T[c]


D(r)
for _ in ' '*q:
    print(T[int(I())])
