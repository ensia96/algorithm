n, d, k, c = map(int, input().split())
A, D, x = [int(input())for _ in ' '*n], [0]*-~d, 0
A += A
for i in range(k):
    x += not D[A[i]]
    D[A[i]] += 1
y = x+(not D[c])
for i in range(n):
    x += not D[A[i+k]]
    D[A[i+k]] += 1
    D[A[i]] -= 1
    x -= not D[A[i]]
    y = max(y, x+(not D[c]))
print(y)
