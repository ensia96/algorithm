n, *A = map(int, open(0).read().split())
c = [*zip(A[:n*2:2], A[1::2])]
for i, d in zip(A[n*2+1::2], A[n*2+2::2]):
    x, y = c[i-1]
    print(sum(abs(x-a)**2+abs(y-b)**2 <= d*d for a, b in c[:i-1]+c[i:]))
