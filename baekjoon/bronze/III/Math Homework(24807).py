b, c, d, l = map(int, input().split())
A = [(i, j, k)for i in range(l//b+1)for j in range(l//c+1)
     for k in range(l//d+1)if i*b+j*c+k*d == l]
for a in (len(A) < 1)*[['impossible']]+A:
    print(*a)
