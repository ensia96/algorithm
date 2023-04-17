n, x, k = map(int, input().split())
A = [0]*-~n
A[x] = 1
for _ in ' '*k:
    a, b = map(int, input().split())
    A[a], A[b] = A[b], A[a]
print(max(-~i for i in range(n)if A[-~i]))
