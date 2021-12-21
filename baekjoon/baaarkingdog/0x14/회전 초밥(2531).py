n, d, k, c = map(int, input().split())
A = [int(input())for _ in ' '*n]
E = [0]*(d+1)
a = j = 0
for i in range(n):
    while j-i < k:
        E[A[j % n]], j = E[A[j % n]]+1, j+1
    a, E[A[i]] = max(a, sum(e > 0 for e in E)+(not E[c])), E[A[i]]-1
print(a)
