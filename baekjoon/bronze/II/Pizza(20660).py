n, *A = map(int, open(s := 0).read().split())
U = A[:n]
i = 1
for _ in ' '*A[n]:
    x = A[n+i]
    s += not any(b in U for b in A[n+i+1:n+i+x+1])
    i += x+1
print(s)
