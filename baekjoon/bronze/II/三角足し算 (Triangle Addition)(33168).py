n, *A = map(int, open(0).read().split())
exec("A=[*map(sum,zip(A,A[1:]))];print(*A);" * ~-n)
