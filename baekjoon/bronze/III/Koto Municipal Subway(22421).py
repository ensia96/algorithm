*A, _, _ = map(int, open(0).read().split())
for d, e in zip(A[::2], A[1::2]):
    print(min(abs((i*i+(d-i)**2)**.5-e)for i in range(d+1)))
