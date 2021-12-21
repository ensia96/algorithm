M = 1000001
n, k = map(int, input().split())
A, c = [0]*M, 0
for _ in ' '*n:
    s, e = map(int, input().split())
    A[s], A[e] = A[s]+1, A[e]-1
for i in range(M):
    c = A[i] = c+A[i]
s = j = 0
for i in range(M):
    while j < M and s < k:
        s, j = s+A[j], j+1
    if s == k:
        exit(print(i, j))
    s -= A[i]
print(0, 0)
