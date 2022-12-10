A = [1, 1, 2, 2, 2, 8]
for i, j in enumerate(map(int, input().split())):
    A[i] -= j
print(*A)
