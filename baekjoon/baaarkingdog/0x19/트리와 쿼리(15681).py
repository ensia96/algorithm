import sys
sys.setrecursionlimit(10**9)
I = sys.stdin.readline
n, r, q = map(int, I().split())
C, T = [[]for _ in ' '*(n+1)], [0]*(n+1)
for _ in ' '*(n-1):
    u, v = map(int, I().split())
    C[u].append(v)
    C[v].append(u)


def D(c):
    T[c] = 1
    for n in C[c]:
        if not T[n]:
            D(n)
            T[c] += T[n]


D(r)
for _ in ' '*q:
    print(T[int(I())])
