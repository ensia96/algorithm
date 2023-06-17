n, *A = map(int, open(0).read().split())
for i in [i for i in range(1, max(A)+1)if i not in A] or ['good job']:
    print(i)
