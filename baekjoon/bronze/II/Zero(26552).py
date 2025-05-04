n, *A = map(int, open(0).read().split())
for a in A:
    a += 1
    while '0' in str(a):
        a += 1
    print(a)
