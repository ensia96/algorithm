n, *A = map(int, open(0).read().split())
for i in range(n):
    a, b, c = A[3*i:3*-~i]
    print(f'Case #{i+1}:', sum(i & j < c for i in range(a)for j in range(b)))
