import collections as C
n, m = map(int, input().split())
R, c = '', 0
for a in [*zip(*[input()for _ in ' '*n])]:
    a, *b = sorted(C.Counter(a).most_common())
    R += a[0]
    c += sum([c for _, c in b]+[0])
print(R)
print(c)
