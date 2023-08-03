n, *A = map(int, open(0).read().split())
x = sum(39 < 5*A[2*i]-3*A[2*i+1]for i in range(n))
print(f"{x}"+'+'*(x == n))
