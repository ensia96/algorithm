n, m = int(input()), 8**8
A = [0]+[*map(int, input().split())]
for i in range(1, n+1):
    for j in range(i):
        A[i] = min(A[i], A[i-j]+A[j])
print(A[n])
