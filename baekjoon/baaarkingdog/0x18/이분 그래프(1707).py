import sys
import collections as c
I, D = sys.stdin.readline, c.deque


def B(i):
    q, S[i] = D([i]), 1
    while q:
        a = q.popleft()
        for i in C[a]:
            if not S[i]:
                S[i] = -S[a]
                q.append(i)
            elif S[i] == S[a]:
                return 0
    return 1


for _ in ' '*int(I()):
    v, e = map(int, I().split())
    v += 1
    C, S, A = [[]for i in ' '*v], [0]*v, 1
    for j in range(e):
        a, b = map(int, I().split())
        C[a].append(b)
        C[b].append(a)
    for k in range(1, v):
        if S[k]:
            continue
        A = B(k)
        if not A:
            break
    print(["NO", "YES"][A])
