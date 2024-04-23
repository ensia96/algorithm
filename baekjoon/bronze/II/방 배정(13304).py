n, k, *A = map(int, open(0).read().split())
R = [0]*6
for i in range(n):
    y = A[i*2+1]-1
    R[[y-A[i*2], 0][y < 2]] += 1
print(sum(-(-r//k)for r in R))
