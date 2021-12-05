m = 10**6
P = [0, 0]+[1]*m
for i in range(m+1):
    if P[i]:
        P[i+i::i] = [0]*(m//i)
for _ in ' '*int(input()):
    n = int(input())
    print(sum(P[i]*P[n-i]for i in range(2, n//2+1)))
