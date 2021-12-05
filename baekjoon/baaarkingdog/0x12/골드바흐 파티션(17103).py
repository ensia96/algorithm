m = 10**6
P = [0, 0]+[1]*m
for i in range(m+1):
    if not P[i]:
        continue
    for j in range(i+i, m+1, i):
        P[j] = 0
for _ in ' '*int(input()):
    n = int(input())
    print(sum(P[i]*P[n-i]for i in range(2, n//2+1)))
