n = int(input())
n += 1
W, A = [0]*n, [0]
for i in range(1, n):
    t, a, *T = map(int, input().split())
    W[i], A = t, A+[T]
for i in range(n):
    W[i] += max(W[j]for j in A[i] or [0])
print(max(W))
