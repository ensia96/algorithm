n, k, *A = map(int, open(0).read().split())
R = [0]*5
for i in range(n):
    y = A[i*2+1]
    R[(y > 2)+2*(y > 4)+A[i*2]*(y > 2)] += 1
print(sum(-(-r//k)for r in R))
