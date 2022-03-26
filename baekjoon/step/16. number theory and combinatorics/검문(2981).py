n = int(input())
A = [int(input())for _ in ' '*n]
a = max(A)-min(A)
L, B = {a}, []
for i in range(2, int(a**.5)+1):
    if not a % i:
        L.add(i)
        L.add(a//i)
for m in L:
    j = A[0] % m
    for x in A:
        if x % m-j:
            break
    else:
        B += m,
print(*sorted(B))
