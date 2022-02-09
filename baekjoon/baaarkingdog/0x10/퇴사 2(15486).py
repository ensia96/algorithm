import sys
I = sys.stdin.readline
n = int(I())
C = [(*map(int, I().split()),)for _ in ' '*n]
D = [0]*-~n
for i in range(n)[::-1]:
    t, p = C[i]
    D[i] = D[i+1]if i+t > n else max(D[i+1], p+D[i+t])
print(D[0])
