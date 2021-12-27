import collections as C
for _ in ' '*int(input()):
    a, c, n = 1, C.defaultdict(int), int(input())
    for _ in ' '*n:
        c[input().split().pop()] += 1
    for k in c:
        a *= c[k]+1
    print(a-1)
