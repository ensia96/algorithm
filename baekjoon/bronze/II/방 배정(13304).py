n, k, *A = map(int, open(0).read().split())
R = [k-1]*6
for i in range(n):
    y = A[i*2+1]
    R[2*(y-1)//2+A[i*2]*(y > 2)] += 1
print(sum(r//k for r in R))
