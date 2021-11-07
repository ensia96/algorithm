n, D = int(input()), [0]
for i in range(1, n+1):
    D += [min(D[i-j**2]for j in range(1, int(i**.5)+1))+1]
print(D[n])
