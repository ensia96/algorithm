n, m = map(int, input().split())
T, M = {}, {}
for _ in ' '*n:
    t, c = input(), int(input())
    T[t] = []
    for _ in ' '*c:
        N = input()
        T[t] += [N]
        M[N] = t
    T[t].sort()
for _ in ' '*m:
    x, y = input(), int(input())
    print(M[x]if y else '\n'.join(T[x]))
