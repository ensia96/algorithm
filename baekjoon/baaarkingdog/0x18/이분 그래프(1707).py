import sys
I = sys.stdin.readline


def B(i):
    q, S[i] = [(i, 0)], 0
    for p, d in q:
        for c in C[p]:
            if S[c] == d:
                return 0
            elif S[c] < 0:
                q += [(c, not d)]
                S[c] = not d
    return 1


for _ in ' '*int(I()):
    v, e = map(int, I().split())
    v += 1
    C, S, A = [[]for _ in ' '*v], [-1]*v, 0
    for _ in ' '*e:
        a, b = map(int, I().split())
        C[a], C[b] = C[a]+[b], C[b]+[a]
    for i in range(1, v):
        if S[i] >= 0:
            continue
        A = B(i)
        if not A:
            break
    print(['NO', 'YES'][A])
