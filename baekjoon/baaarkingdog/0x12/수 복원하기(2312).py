M = 10**5
P, m = [0, 0]+[1]*(M-1), int(M**.5)
for i in range(m):
    if P[i]:
        P[i+i::i] = [0]*(M//i-1)
P = [i for i in range(m+1)if P[i]]
for _ in ' '*int(input()):
    n = int(input())
    for p in P:
        c = 0
        while not n % p:
            n, c = n//p, c+1
        c and print(p, c)
