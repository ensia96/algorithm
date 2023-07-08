n, *L = map(int, open(0))
A = [0]*n
for i in range(n):
    A[L[i]-1] = i+1
for a in A:
    print(a)
