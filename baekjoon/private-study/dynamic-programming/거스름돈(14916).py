n = int(input())
D = [-1]*100001
D[2] = D[5] = 1
for i in range(n+1):
    if D[i-2] > 0:
        D[i] = D[i-2]+1
    if D[i-5] > 0:
        D[i] = D[i-5]+1
print(D[n])
