n = int(input())
if n < 2:
    exit(print(0))
A = [0, 0]+[1]*(n-1)
for i in range(2, n+1):
    if A[i]:
        A[i+i::i] = [0]*(n//i-1)
A = [i for i in range(n+1)if A[i]]
r, s, c, j = len(A), A[0], 0, 1
for i in range(r):
    while j < r and s < n:
        s, j = s+A[j], j+1
    c, s = c+(s == n), s-A[i]
print(c)
