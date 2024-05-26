n, m, *A = map(int, open(0).read().split())
x = 0
for i in range(n):
    for b in A[n+x:]:
        if A[i] < b:
            break
        A[i] -= b
        x += 1
print(sum(A[:n]))
