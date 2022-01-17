import sys
sys.setrecursionlimit(100000)
I = sys.stdin.readline
n, r, q = map(int, I().split())
C, T = [[]for _ in ' '*(n+1)], [0]*(n+1)
for _ in ' '*(n-1):
    u, v = map(int, I().split())
    C[u].append(v)
    C[v].append(u)


def D(c, p): T[c] = sum(n != p and D(n, c)for n in C[c])+1; return T[c]


D(r, 0)
for _ in ' '*q:
    print(T[int(I())])
