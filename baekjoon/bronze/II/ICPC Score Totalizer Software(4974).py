*A, = map(int, open(i := 0))
while n := A[i]:
    print(sum(sorted(A[i+1:i+n+1])[1:-1])//(n-2))
    i += n+1
