n, m = map(int, input().split())
A = [0]*n
for _ in ' '*m:
    a, b = map(int, input().split())
    A[a-1] += 1
    A[b-1] += 1
print(*A)
