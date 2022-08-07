n, m = map(int, input().split())
E = [[]for _ in ' '*-~n]
A = [1]*-~n
for _ in ' '*m:
    a, b = map(int, input().split())
    E[b] += a,
for i in range(1, n+1):
    A[i] = max([A[j]for j in E[i]]+[0])+1
print(*A[1:])
