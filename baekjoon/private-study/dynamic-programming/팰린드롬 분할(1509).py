import heapq as H
A = input()
n = len(A)
C = [[0]*n for _ in ' '*n]
for j in range(n):
    for i in range(n-j):
        m = A[i] == A[i+j]
        C[i][i+j] = not j or (j == 1)*m or m*C[i+1][i+j-1]
E = {i: [j+1 for j in range(i, n)if C[i][j]]for i in range(n)}
Q = [(0, 0)]
m = 8**8
D = [0]+[m]*-~n
while Q:
    x, y = H.heappop(Q)
    if D[y]-x:
        continue
    for i in E.get(y, []):
        if D[i] > D[y]+1:
            D[i] = D[y]+1
            H.heappush(Q, (D[i], i))
print(D[-1])
