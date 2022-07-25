n, k = map(int, input().split())
A = [*map(int, input().split())]
r = s = sum(A[:k])
for i in range(k, n):
    s += A[i]-A[i-k]
    r = max(s, r)
print(r)
