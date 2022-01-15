import sys
I = sys.stdin.readline
n, k, m = map(int, I().split())
L = [[]for _ in ' '*(n+m+1)]
for i in range(m):
    for j in map(int, I().split()):
        L[j].append(n+i+1)
        L[n+i+1].append(j)
Q, V = [1], [0, 1]+[0]*(n+m-1)
for i in Q:
    if i == n:
        exit(print(V[i]))
    for s in L[i]:
        if not V[s]:
            Q.append(s)
            V[s] = V[i]+(s > n)
print(-1)
