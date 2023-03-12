A = [0, 1, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    A[a], A[b] = A[b], A[a]
print(max(i*A[i]for i in range(4)))
