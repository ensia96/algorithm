input()
(*A,) = map(int, input().split())
i, *T = [0]
while i < len(A):
    a = A[i]
    i += a
    T += (a,)
print(*T)
