n = int(input())
A = [*map(int, input().split())]
V = [0]*100001
a = j = 0
for i in range(n):
    while j < n and not V[A[j]]:
        V[A[j]], j = V[A[j]]+1, j+1
    a, V[A[i]] = a+j-i, V[A[i]]-1
print(a)
