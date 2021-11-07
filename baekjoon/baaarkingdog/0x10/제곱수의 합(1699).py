n = int(input())
D = [*range(n+1)]
for i in range(2, n+1):
    for j in range(i):
        if j*j > i:
            break
        D[i] = min(D[i], D[i-j*j]+1)
print(D[n])
