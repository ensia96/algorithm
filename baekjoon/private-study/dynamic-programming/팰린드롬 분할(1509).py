A = input()
n = len(A)
D = [*range(n+1)]
if A == A[::-1]:
    exit(print(1))
for i in range(n):
    for j in range(i+1, n+1):
        t = A[i:j]
        if t == t[::-1]:
            D[j] = min(D[j], D[i]+1)
print(D[-1])
