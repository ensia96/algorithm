n, *A = map(int, open(0).read().split())
for a in A[n+1:]:
    A[a-1] -= 1
for a in A[:n]:
    print('yneos'[a >= 0::2])
