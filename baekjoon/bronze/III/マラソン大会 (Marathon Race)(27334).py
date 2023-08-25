n, *A = map(int, open(0).read().split())
for a in map(sorted(A).index, A):
    print(a+1)
