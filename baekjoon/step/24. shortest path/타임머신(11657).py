l, M = lambda: map(int, input().split()), 8**8
n, m = l()
D = [M]*-~n
E = [[*l()]for _ in ' '*m]
D[1] = 0
for i in range(n):
    for u, v, w in E:
        if D[u]-M and D[v] > D[u]+w:
            if i == n-1:
                exit(print(-1))
            D[v] = D[u]+w
for i in D[2:]:
    print(i if i-M else -1)
