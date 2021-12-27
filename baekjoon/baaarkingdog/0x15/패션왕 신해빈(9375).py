import itertools as i
import collections as c
C, D = i.combinations, c.defaultdict
for _ in ' '*int(input()):
    c, n = D(int), int(input())
    for _ in ' '*n:
        c[input().split().pop()] += 1
    A, K = n, c.keys()
    for i in range(1, len(K)):
        a = 1
        for x in C(K, i+1):
            for k in x:
                a *= c[k]
        A += a
    print(A)
