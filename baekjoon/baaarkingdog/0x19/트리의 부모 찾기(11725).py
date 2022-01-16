n = int(input())
C = [[]for _ in ' '*(n+1)]
for _ in ' '*(n-1):
    a, b = map(int, input().split())
    C[a], C[b] = C[a]+[b], C[b]+[a]
S, P = [1], [0]*(n+1)
while S:
    c = S.pop()
    for i in C[c]:
        if P[c] == i:
            continue
        P[i] = c
        S += [i]
for p in P[2:]:
    print(p)
