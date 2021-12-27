import collections as c
for _ in ' '*int(input()):
    a, c, n = 1, c.defaultdict(int), int(input())
    for _ in ' '*n:
        c[input().split().pop()] += 1
    for k in c:
        a *= c[k]+1
    print(a-1)
