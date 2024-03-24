n = int(input())
A = [*range(1, n+1)]
while len(A) > 1:
    A = A[1::2]
print(*A)
