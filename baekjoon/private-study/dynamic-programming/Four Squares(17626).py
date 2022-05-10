n = int(input())
D = [0, 1]+[4]*n
for i in range(1, n+1):
    D[i] = min(1+D[i-j*j]for j in range(1, int(i**.5)+1))
print(D[n])
