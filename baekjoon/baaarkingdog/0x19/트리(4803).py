T = 1
while T:
    n, m = map(int, input().split())
    if not n+m:
        break
    n += 1
    A, C, V = 0, [[]for _ in ' '*n], [0]*n
    for _ in ' '*m:
        a, b = map(int, input().split())
        C[a].append(b)
        C[b].append(a)
    for i in range(1, n):
        if V[i]:
            continue
        A, S, F = A+1, [(i, 0)], 0
        while S:
            c, p = S.pop()
            V[c] = 1
            for j in C[c]:
                if j == p:
                    continue
                F = F or V[j]
                if not V[j]:
                    S.append((j, c))
        A -= F
    if A > 1:
        A = f'A forest of {A} trees.'
    elif A > 0:
        A = 'There is one tree.'
    else:
        A = 'No trees.'
    print(f"Case {T}:", A)
    T += 1
