import collections as C
n = int(input())+1
C, I, E, R, Q = [0]*n, [0]*n, [[]for _ in ' '*n], [0]*n, C.deque()
N = range(1, n)
for i in N:
    c, *A = map(int, input().split())
    C[i] = c
    for a in A[:-1]:
        E[a] += i,
        I[i] += 1
for i in N:
    if not I[i]:
        Q += i,
while Q:
    c = Q.popleft()
    R[c] += C[c]
    for e in E[c]:
        I[e] -= 1
        R[e] = max(R[e], R[c])
        if not I[e]:
            Q += e,
for r in R[1:]:
    print(r)
