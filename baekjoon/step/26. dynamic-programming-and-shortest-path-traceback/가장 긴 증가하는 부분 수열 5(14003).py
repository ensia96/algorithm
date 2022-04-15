import bisect as B
n = int(input())
A = [0]+[*map(int, input().split())]
D = [0]*-~n
C = [0]
R = []
M = 0

for i in range(1, n+1):
    if C[-1] < A[i]:
        M = D[i] = len(C)
        C += A[i],
        continue
    D[i] = B.bisect_left(C, A[i])
    C[D[i]] = A[i]
print(M)
for i in range(n, 0, -1):
    if D[i] == M:
        R += A[i],
        M -= 1
print(*R[::-1])
