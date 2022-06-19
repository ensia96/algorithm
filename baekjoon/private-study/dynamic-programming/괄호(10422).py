M = 1000000007
D = [1]+[0]*2500
for i in range(1, 2501):
    D[i] = (sum(D[i-k-1]*D[k] % M for k in range(i+1))) % M
for _ in ' '*int(input()):
    n = int(input())
    print(~-(n % 2) and D[n//2])
