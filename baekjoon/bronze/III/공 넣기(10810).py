n, m = map(int, input().split())
A = [0]*n
for _ in ' '*m:
    i, j, k = map(int, input().split())
    A[i-1:j] = [k]*(j-i+1)
print(*A)
