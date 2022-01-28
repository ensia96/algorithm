n = int(input())
n += 1
W, A = [0]*n, [()]
for i in range(1, n):
    t, a, *T = map(int, input().split())
    W[i], A = t, A+[T]
for i in range(2, n):
    W[i] += max(W[j]for j in A[i])
print(max(W))
