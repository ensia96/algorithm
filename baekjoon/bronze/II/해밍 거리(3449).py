A = open(0).read().split()[1:]
for a, b in zip(A[::2], A[1::2]):
    print(f'Hamming distance is {sum(a[i]!=b[i]for i in range(len(a)))}.')
