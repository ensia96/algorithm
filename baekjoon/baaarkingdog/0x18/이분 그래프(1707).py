import sys
I = sys.stdin.readline
for _ in ' '*int(I()):
    v, e = map(int, I().split())
    v += 1
    C, S = [[]for _ in ' '*v], [-1]*v
    for _ in ' '*e:
        a, b = map(int, I().split())
        C[a], C[b] = C[a]+[b], C[b]+[a]
    for i in range(1, v):
        if S[i] >= 0:
            continue
        q, S[i] = [(i, 0)], 0
        for p, d in q:
            for c in C[p]:
                if S[c] == d:
                    print('NO')
                    break
                elif S[c] < 0:
                    q += [(c, not d)]
                    S[c] = not d
            else:
                continue
            break
        else:
            continue
        break
    else:
        print('YES')
