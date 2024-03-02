n, m, l = map(int, input().split())
i, *A = [0]*-~n
while A[i]+1 < m:
    A[i] += 1
    i = (i+l*(2*(A[i] % 2)-1)) % n
print(sum(A))
