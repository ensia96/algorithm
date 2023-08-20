n, *A = map(int, open(0).read().split())
for a in {*A}:
    A.count(a) < 2 and print(a)
