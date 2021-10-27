n, A = int(input()), [0]+[*map(int, input().split())]
d = [0]*(n+1)
for i in range(1, n+1):
    for j in range(i):
        d[i] = [d[i], max(d[j]+A[i], d[i])][A[i] > A[j]]
print(max(d))
