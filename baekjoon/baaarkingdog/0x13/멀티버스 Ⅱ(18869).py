import sys
m, n = map(int, input().split())
D = {}
for _ in ' '*m:
    *l, = map(int, sys.stdin.readline().split())
    d = {j: i for i, j in enumerate(sorted([*set(l)]))}
    k = (*(d[i]for i in l),)
    D[k] = D.get(k, 0)+1
print(sum(i*~-i//2 for i in D.values()))
