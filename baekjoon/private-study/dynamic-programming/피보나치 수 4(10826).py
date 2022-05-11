n = int(input())
D = [0, 1]+[0]*n
for i in range(2, n+1):
    D[i] = D[i-1]+D[i-2]
print(D[n])
