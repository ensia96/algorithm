a, b, *A = open(0).read().split()
x = int(a)
for a in A[:x]:
    for b in A[x:]:
        print(a, 'as', b)
