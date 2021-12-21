n, k = map(int, input().split())
A = [*map(int, input().split())]
C = [0]*100001
a = j = 0
for i in range(n):
    while j < n and C[A[j]] < k:
        C[A[j]], j = C[A[j]]+1, j+1
    C[A[i]], a = C[A[i]]-1, max(a, j-i)
print(a)
